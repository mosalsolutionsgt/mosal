import sys

js_path = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/js/cotizador.js"

with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# 1. State changes
old_state = """        prendas: {
            prenda: null,
            estilo: null,
            tecnica: null,
            colorBase: null,
            cantidades: { XS: 0, S: 0, M: 0, L: 0, XL: 0, XXL: 0, '3XL': 0 },
            totalQty: 0
        },"""
new_state = """        prendas: {
            prenda: null,
            estilo: null,
            tecnica: null,
            tamanoDiseno: null,
            colorBase: null,
            cantidades: { XS: 0, S: 0, M: 0, L: 0, XL: 0, XXL: 0, '3XL': 0 },
            totalQty: 0
        },
        stickers: {
            size: null,
            pricePer100: 0,
            qtyHundreds: 1
        },
        otros: {
            desc: null
        },"""
js_content = js_content.replace(old_state, new_state)

# 2. Flows and elements
old_flows = """        galardones: ['step_category', 'step_galardones_1', 'step_galardones_2', 'step_design', 'step_summary', 'step_contact'],
        dtf_uv: ['step_category', 'step_dtf_1', 'step_design', 'step_summary', 'step_contact']
    };"""
new_flows = """        galardones: ['step_category', 'step_galardones_1', 'step_galardones_2', 'step_design', 'step_summary', 'step_contact'],
        dtf_uv: ['step_category', 'step_dtf_1', 'step_design', 'step_summary', 'step_contact'],
        stickers: ['step_category', 'step_stickers_1', 'step_design', 'step_summary', 'step_contact'],
        otros: ['step_category', 'step_otros_1', 'step_design', 'step_summary', 'step_contact']
    };"""
js_content = js_content.replace(old_flows, new_flows)

# Add elements
old_elem_start = """    const elements = {"""
new_elem_start = """    const elements = {
        tamanoDisenoGroup: document.getElementById('tamanoDisenoGroup'),
        tamanoDisenoCards: document.querySelectorAll('#tamanoDisenoCards .card-option'),
        stickerSize: document.getElementById('stickerSize'),
        stickerQty: document.getElementById('stickerQty'),
        otrosText: document.getElementById('otrosText'),"""
js_content = js_content.replace(old_elem_start, new_elem_start)

# 3. New event listeners
old_tecnica_cards = """    elements.tecnicaCards.forEach(card => {
        card.addEventListener('click', () => {
            elements.tecnicaCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            state.prendas.tecnica = card.querySelector('h3').textContent;
            validateStep();
        });
    });"""

new_tecnica_cards = """    elements.tecnicaCards.forEach(card => {
        card.addEventListener('click', () => {
            elements.tecnicaCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            state.prendas.tecnica = card.querySelector('h3').textContent;
            
            // Mostrar u ocultar Tamaño de diseño
            if (state.prendas.tecnica === 'Sublimación') {
                elements.tamanoDisenoGroup.style.display = 'none';
                state.prendas.tamanoDiseno = null;
            } else {
                elements.tamanoDisenoGroup.style.display = 'block';
            }
            
            validateStep();
        });
    });

    if(elements.tamanoDisenoCards) {
        elements.tamanoDisenoCards.forEach(card => {
            card.addEventListener('click', () => {
                elements.tamanoDisenoCards.forEach(c => c.classList.remove('selected'));
                card.classList.add('selected');
                state.prendas.tamanoDiseno = card.dataset.value;
                validateStep();
            });
        });
    }
    
    if(elements.stickerSize) {
        elements.stickerSize.addEventListener('change', (e) => {
            state.stickers.size = e.target.value;
            state.stickers.pricePer100 = parseInt(e.target.options[e.target.selectedIndex].dataset.price);
            validateStep();
        });
        elements.stickerQty.addEventListener('input', (e) => {
            state.stickers.qtyHundreds = parseInt(e.target.value) || 1;
            validateStep();
        });
    }
    
    if(elements.otrosText) {
        elements.otrosText.addEventListener('input', (e) => {
            state.otros.desc = e.target.value;
            validateStep();
        });
    }"""
js_content = js_content.replace(old_tecnica_cards, new_tecnica_cards)

# 4. Validations
old_val = """        if (currentStepId === 'step_prendas_1') {
            isValid = state.prendas.prenda !== null;
        } else if (currentStepId === 'step_prendas_2') {
            isValid = state.prendas.estilo !== null && state.prendas.tecnica !== null;
        } else if (currentStepId === 'step_prendas_3') {"""
new_val = """        if (currentStepId === 'step_prendas_1') {
            isValid = state.prendas.prenda !== null;
        } else if (currentStepId === 'step_prendas_2') {
            isValid = state.prendas.estilo !== null && state.prendas.tecnica !== null;
            if (state.prendas.tecnica !== 'Sublimación' && state.prendas.tamanoDiseno === null) {
                isValid = false;
            }
        } else if (currentStepId === 'step_prendas_3') {
            isValid = state.prendas.totalQty > 0 && state.prendas.colorBase !== null;
        } else if (currentStepId === 'step_stickers_1') {
            isValid = state.stickers.size !== null && state.stickers.qtyHundreds > 0;
        } else if (currentStepId === 'step_otros_1') {
            isValid = state.otros.desc !== null && state.otros.desc.trim().length > 0;
        } else if (currentStepId === 'step_uniformes_1') {"""
js_content = js_content.replace(old_val, new_val)

# 5. Calculate Total
old_calc = """    function calculateTotal() {
        let total = 0;
        if (state.category === 'prendas') {
            if (state.prendas.prenda === 'Playera / Polo' && state.prendas.estilo === 'T-Shirt Normal' && state.prendas.totalQty >= 25) {
                for (let [size, qty] of Object.entries(state.prendas.cantidades)) {
                    let price = 50;
                    if (['XL', 'XXL', '3XL'].includes(size)) {
                        price += 10;
                    }
                    total += price * qty;
                }
            } else if (state.prendas.prenda === 'Playera / Polo' && (state.prendas.estilo === 'Polo Hombre' || state.prendas.estilo === 'Polo Mujer')) {
                for (let [size, qty] of Object.entries(state.prendas.cantidades)) {
                    let price = 115;
                    if (['L', 'XL', 'XXL', '3XL'].includes(size)) {
                        price = 125;
                    }
                    total += price * qty;
                }
            } else if (state.prendas.prenda === 'Sudadera' && state.prendas.estilo === 'Hoodie con Bolsa') {
                for (let [size, qty] of Object.entries(state.prendas.cantidades)) {
                    total += 155 * qty;
                }
            } else {
                total = 0; // Precios pendientes (Oversize, Sin bolsa, Zipper, Gorras)
            }
        } else if (state.category === 'uniformes') {"""
        
new_calc = """    function calculateTotal() {
        let total = 0;
        let requiresConfirmation = false;
        
        if (state.category === 'prendas') {
            let baseGarmentPrice = 0;
            let extraSizeCost = 0;
            
            if (state.prendas.prenda === 'Playera / Polo' && state.prendas.estilo === 'T-Shirt Normal') {
                baseGarmentPrice = 42;
                extraSizeCost = 10; // para XL+
            } else if (state.prendas.prenda === 'Playera / Polo' && (state.prendas.estilo === 'Polo Hombre' || state.prendas.estilo === 'Polo Mujer')) {
                baseGarmentPrice = 90;
                extraSizeCost = 10; // para L+
            } else if (state.prendas.prenda === 'Sudadera' && state.prendas.estilo === 'Hoodie con Bolsa') {
                baseGarmentPrice = 130;
                extraSizeCost = 0; // Se asume parejo, si no, se sumaría
            } else {
                requiresConfirmation = true; // Gorras u otros sudaderos
            }

            // Técnica de Impresión
            let techPrice = 0;
            let qty = state.prendas.totalQty;
            let tamano = state.prendas.tamanoDiseno;
            let tech = state.prendas.tecnica;
            let fixedTechCost = 0;

            if (tech === 'Sublimación') {
                requiresConfirmation = true;
            } else if (tech === 'DTF') {
                if (tamano === '10 cm') techPrice = (qty >= 25) ? 8 : 10;
                else if (tamano === '15 - 20 cm') techPrice = (qty >= 25) ? 15 : 20;
                else if (tamano === '25 cm') techPrice = (qty >= 25) ? 25 : 30;
            } else if (tech === 'Vinil Textil') {
                if (tamano === '10 cm') techPrice = (qty >= 25) ? 20 : 25;
                else requiresConfirmation = true; // tamaños mayores sujetos a ver imagen
            } else if (tech === 'Bordado') {
                if (tamano === '10 cm') {
                    techPrice = 25;
                    if (qty > 0 && qty < 6) {
                        fixedTechCost = 50; // costo de digitalización
                    }
                } else {
                    requiresConfirmation = true;
                }
            }
            
            if (!requiresConfirmation && baseGarmentPrice > 0 && qty > 0) {
                for (let [size, sizeQty] of Object.entries(state.prendas.cantidades)) {
                    let currentBase = baseGarmentPrice;
                    if (state.prendas.estilo === 'T-Shirt Normal' && ['XL', 'XXL', '3XL'].includes(size)) {
                        currentBase += extraSizeCost;
                    } else if ((state.prendas.estilo === 'Polo Hombre' || state.prendas.estilo === 'Polo Mujer') && ['L', 'XL', 'XXL', '3XL'].includes(size)) {
                        currentBase += extraSizeCost;
                    }
                    total += (currentBase + techPrice) * sizeQty;
                }
                total += fixedTechCost;
            } else {
                total = 0; // Muestra 'Por confirmar'
            }
            
        } else if (state.category === 'stickers') {
            total = state.stickers.pricePer100 * state.stickers.qtyHundreds;
        } else if (state.category === 'otros') {
            total = 0; // Siempre por confirmar
        } else if (state.category === 'uniformes') {"""
js_content = js_content.replace(old_calc, new_calc)

# 6. Summary updates
old_summary = """        if (state.category === 'prendas') {
            html = `
                <div class="summary-row"><span>Categoría:</span><strong>Prendas Personalizadas</strong></div>
                <div class="summary-row"><span>Prenda:</span><strong>${state.prendas.prenda}</strong></div>
                <div class="summary-row"><span>Estilo:</span><strong>${state.prendas.estilo}</strong></div>
                <div class="summary-row"><span>Técnica:</span><strong>${state.prendas.tecnica}</strong></div>
                <div class="summary-row"><span>Color Base:</span><strong>${state.prendas.colorBase}</strong></div>
                <div class="summary-row"><span>Cantidad Total:</span><strong>${state.prendas.totalQty}</strong></div>
            `;
        } else if (state.category === 'uniformes') {"""

new_summary = """        if (state.category === 'prendas') {
            html = `
                <div class="summary-row"><span>Categoría:</span><strong>Prendas Personalizadas</strong></div>
                <div class="summary-row"><span>Prenda:</span><strong>${state.prendas.prenda}</strong></div>
                <div class="summary-row"><span>Estilo:</span><strong>${state.prendas.estilo}</strong></div>
                <div class="summary-row"><span>Técnica:</span><strong>${state.prendas.tecnica}</strong></div>
                ${state.prendas.tamanoDiseno ? `<div class="summary-row"><span>Tamaño Diseño:</span><strong>${state.prendas.tamanoDiseno}</strong></div>` : ''}
                <div class="summary-row"><span>Color Base:</span><strong>${state.prendas.colorBase}</strong></div>
                <div class="summary-row"><span>Cantidad Total:</span><strong>${state.prendas.totalQty}</strong></div>
            `;
        } else if (state.category === 'stickers') {
            html = `
                <div class="summary-row"><span>Categoría:</span><strong>Stickers Personalizados</strong></div>
                <div class="summary-row"><span>Medida:</span><strong>${state.stickers.size} cm</strong></div>
                <div class="summary-row"><span>Cantidad:</span><strong>${state.stickers.qtyHundreds} Cientos (${state.stickers.qtyHundreds * 100} un.)</strong></div>
            `;
        } else if (state.category === 'otros') {
            html = `
                <div class="summary-row"><span>Categoría:</span><strong>Otros Productos</strong></div>
                <div class="summary-row"><span>Descripción:</span><strong>${state.otros.desc}</strong></div>
            `;
        } else if (state.category === 'uniformes') {"""
js_content = js_content.replace(old_summary, new_summary)

# 7. WhatsApp message updates
old_msg = """        if (state.category === 'prendas') {
            let sizesStr = Object.entries(state.prendas.cantidades).filter(([_, qty]) => qty > 0).map(([size, qty]) => `${qty} talla ${size}`).join(', ');
            msg += `- Categoría: Prendas Personalizadas%0A- Prenda: ${state.prendas.prenda} (${state.prendas.estilo})%0A- Técnica: ${state.prendas.tecnica}%0A- Color Base: ${state.prendas.colorBase}%0A- Cantidades: ${sizesStr} (Total: ${state.prendas.totalQty})%0A`;
        } else if (state.category === 'uniformes') {"""

new_msg = """        if (state.category === 'prendas') {
            let sizesStr = Object.entries(state.prendas.cantidades).filter(([_, qty]) => qty > 0).map(([size, qty]) => `${qty} talla ${size}`).join(', ');
            msg += `- Categoría: Prendas Personalizadas%0A- Prenda: ${state.prendas.prenda} (${state.prendas.estilo})%0A- Técnica: ${state.prendas.tecnica}%0A`;
            if (state.prendas.tamanoDiseno) msg += `- Tamaño Diseño: ${state.prendas.tamanoDiseno}%0A`;
            msg += `- Color Base: ${state.prendas.colorBase}%0A- Cantidades: ${sizesStr} (Total: ${state.prendas.totalQty})%0A`;
        } else if (state.category === 'stickers') {
            msg += `- Categoría: Stickers Personalizados%0A- Medida: ${state.stickers.size} cm%0A- Cantidad: ${state.stickers.qtyHundreds} Cientos (${state.stickers.qtyHundreds * 100} unidades)%0A`;
        } else if (state.category === 'otros') {
            msg += `- Categoría: Otros Productos%0A- Detalles: ${state.otros.desc}%0A`;
        } else if (state.category === 'uniformes') {"""
js_content = js_content.replace(old_msg, new_msg)

# 8. Polo charts fix
old_charts = """                { name: 'Polo Hombre', img: 'assets/mockups/prendas/page_8_img_0.png', chart: 'assets/mockups/prendas/page_11_img_0.png' },
                { name: 'Polo Mujer', img: 'assets/mockups/prendas/page_8_img_0.png', chart: 'assets/mockups/prendas/page_12_img_0.png' }"""
new_charts = """                { name: 'Polo Hombre', img: 'assets/mockups/prendas/page_8_img_0.png', chart: 'assets/mockups/prendas/polo_hombre_chart.png' },
                { name: 'Polo Mujer', img: 'assets/mockups/prendas/page_8_img_0.png', chart: 'assets/mockups/prendas/polo_mujer_chart.png' }"""
js_content = js_content.replace(old_charts, new_charts)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("JS Patched.")
