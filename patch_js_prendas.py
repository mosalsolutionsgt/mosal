new_js = """document.addEventListener('DOMContentLoaded', () => {
    // State Machine
    const state = {
        category: null, 
        currentStepIndex: 0, 
        flow: [], 
        
        // Data Prendas
        prendas: {
            prenda: null,
            estilo: null,
            tecnica: null,
            colorBase: null,
            cantidades: { XS: 0, S: 0, M: 0, L: 0, XL: 0, XXL: 0, '3XL': 0 },
            totalQty: 0
        },
        // Data Uniformes
        uniformes: {
            prenda: null,
            prendaDesc: null,
            basePrice: 0,
            tecnica: null,
            reflectivo: '1 Pulgada',
            colorBase: null,
            cantidades: {},
            totalQty: 0
        },
        // Data Galardones
        galardones: {
            ref: null,
            desc: null,
            cantidad: 1,
            unitPrice: 0
        },
        // Data DTF UV
        dtf: {
            ancho: '28cm',
            metros: 1,
            basePrice: 120
        },
        
        file: null,
        estimatedTotal: 0
    };

    const WHATSAPP_NUMBER = '50230292980'; 

    // Elements
    const elements = {
        progressContainer: document.getElementById('progressContainer'),
        progressFill: document.getElementById('progressFill'),
        progressSteps: document.getElementById('progressSteps'),
        btnPrev: document.getElementById('btnPrev'),
        btnNext: document.getElementById('btnNext'),
        btnWhatsapp: document.getElementById('btnWhatsapp'),
        btnEmail: document.getElementById('btnEmail'),
        
        // Category
        categoryCards: document.querySelectorAll('.category-card'),
        
        // Prendas
        prendaCards: document.querySelectorAll('#prendaCards .card-option'),
        prendasEstilosGrid: document.getElementById('prendasEstilosGrid'),
        tecnicaCards: document.querySelectorAll('#tecnicaCards .card-option'),
        colorOptions: document.querySelectorAll('#colorPicker .color-option'),
        selectedColorDisplay: document.getElementById('selectedColorDisplay'),
        qtyInputs: document.querySelectorAll('.qty-input'),
        totalQtyDisplay: document.getElementById('totalQty'),
        
        // Uniformes
        uniformeCards: document.querySelectorAll('#uniformeCards .card-option'),
        uniTecnicaCards: document.querySelectorAll('#uniTecnicaCards .card-option'),
        uniReflectivoCards: document.querySelectorAll('#uniReflectivoCards .card-option'),
        uniColorOptions: document.querySelectorAll('#uniColorPicker .color-option'),
        uniSelectedColorDisplay: document.getElementById('uniSelectedColorDisplay'),
        uniColorGroup: document.getElementById('uniColorGroup'),
        uniSizesGrid: document.getElementById('uniSizesGrid'),
        uniTotalQtyDisplay: document.getElementById('uniTotalQty'),

        // Galardones
        galardonesCards: document.querySelectorAll('#galardonesCards .card-option'),
        galardonesQty: document.getElementById('galardonesQty'),
        
        // DTF
        dtfQty: document.getElementById('dtfQty'),
        
        // Shared
        dropzone: document.getElementById('dropzone'),
        fileInput: document.getElementById('fileInput'),
        browseBtn: document.getElementById('browseBtn'),
        filePreview: document.getElementById('filePreview'),
        fileName: document.getElementById('fileName'),
        fileSize: document.getElementById('fileSize'),
        removeFileBtn: document.getElementById('removeFileBtn'),

        summaryPanelContainer: document.getElementById('summaryPanelContainer'),

        userName: document.getElementById('userName'),
        userPhone: document.getElementById('userPhone'),
        userEmail: document.getElementById('userEmail'),
        userNotes: document.getElementById('userNotes')
    };

    // Flow definitions
    const flows = {
        prendas: ['step_category', 'step_prendas_1', 'step_prendas_2', 'step_prendas_3', 'step_design', 'step_summary', 'step_contact'],
        uniformes: ['step_category', 'step_uniformes_1', 'step_uniformes_2', 'step_uniformes_3', 'step_design', 'step_summary', 'step_contact'],
        galardones: ['step_category', 'step_galardones_1', 'step_galardones_2', 'step_design', 'step_summary', 'step_contact'],
        dtf_uv: ['step_category', 'step_dtf_1', 'step_design', 'step_summary', 'step_contact']
    };

    state.flow = ['step_category']; 
    
    // Category Selection
    elements.categoryCards.forEach(card => {
        card.addEventListener('click', () => {
            elements.categoryCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            state.category = card.dataset.category;
            
            state.flow = flows[state.category];
            state.currentStepIndex = 1; 
            
            buildProgressIndicators();
            updateWizardUI();
        });
    });

    function buildProgressIndicators() {
        elements.progressContainer.classList.remove('hidden');
        elements.progressSteps.innerHTML = '';
        const numSteps = state.flow.length - 1; 
        for (let i = 1; i <= numSteps; i++) {
            const span = document.createElement('span');
            span.className = 'step-indicator';
            span.textContent = i;
            elements.progressSteps.appendChild(span);
        }
    }

    // Navigation logic
    function updateWizardUI() {
        document.querySelectorAll('.wizard-step').forEach(step => step.classList.remove('active'));
        
        const currentStepId = state.flow[state.currentStepIndex];
        const currentStepEl = document.getElementById(currentStepId);
        if (currentStepEl) {
            currentStepEl.classList.add('active');
        }

        if (state.currentStepIndex > 0) {
            elements.progressContainer.classList.remove('hidden');
            const indicators = elements.progressSteps.querySelectorAll('.step-indicator');
            indicators.forEach((indicator, index) => {
                indicator.classList.remove('active', 'completed');
                if (index + 1 < state.currentStepIndex) {
                    indicator.classList.add('completed');
                } else if (index + 1 === state.currentStepIndex) {
                    indicator.classList.add('active');
                }
            });

            const numSteps = state.flow.length - 1;
            const progress = ((state.currentStepIndex - 1) / (numSteps - 1)) * 100;
            elements.progressFill.style.width = `${progress}%`;
        } else {
            elements.progressContainer.classList.add('hidden');
        }

        elements.btnPrev.classList.toggle('hidden', state.currentStepIndex === 0);
        elements.btnNext.classList.toggle('hidden', state.currentStepIndex === 0 || state.currentStepIndex === state.flow.length - 1);
        
        const isLastStep = state.currentStepIndex === state.flow.length - 1;
        elements.btnWhatsapp.classList.toggle('hidden', !isLastStep);
        elements.btnEmail.classList.toggle('hidden', !isLastStep);

        if (currentStepId === 'step_summary') {
            updateSummary();
        }

        validateStep();
    }

    elements.btnNext.addEventListener('click', () => {
        if (validateStep() && state.currentStepIndex < state.flow.length - 1) {
            state.currentStepIndex++;
            updateWizardUI();
        }
    });

    elements.btnPrev.addEventListener('click', () => {
        if (state.currentStepIndex > 0) {
            state.currentStepIndex--;
            updateWizardUI();
        }
    });

    // Validations
    function validateStep() {
        let isValid = true;
        const currentStepId = state.flow[state.currentStepIndex];
        
        if (currentStepId === 'step_prendas_1') {
            isValid = state.prendas.prenda !== null;
        } else if (currentStepId === 'step_prendas_2') {
            isValid = state.prendas.estilo !== null && state.prendas.tecnica !== null;
        } else if (currentStepId === 'step_prendas_3') {
            isValid = state.prendas.totalQty > 0 && state.prendas.colorBase !== null;
        } else if (currentStepId === 'step_uniformes_1') {
            isValid = state.uniformes.prenda !== null;
        } else if (currentStepId === 'step_uniformes_2') {
            isValid = state.uniformes.tecnica !== null && state.uniformes.reflectivo !== null;
        } else if (currentStepId === 'step_uniformes_3') {
            const isCamisa = state.uniformes.prenda && state.uniformes.prenda.includes('CAMISA');
            if (isCamisa) {
                isValid = state.uniformes.totalQty > 0 && state.uniformes.colorBase !== null;
            } else {
                isValid = state.uniformes.totalQty > 0;
            }
        } else if (currentStepId === 'step_galardones_1') {
            isValid = state.galardones.ref !== null;
        } else if (currentStepId === 'step_galardones_2') {
            isValid = state.galardones.cantidad > 0;
        } else if (currentStepId === 'step_dtf_1') {
            isValid = state.dtf.metros > 0;
        }

        elements.btnNext.disabled = !isValid;
        return isValid;
    }

    // --- PRENDAS INTERACTIONS ---
    elements.prendaCards.forEach(card => {
        card.addEventListener('click', () => {
            elements.prendaCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            state.prendas.prenda = card.querySelector('h3').textContent;
            
            // Build Estilos dynamically
            buildPrendasEstilos(state.prendas.prenda);
            state.prendas.estilo = null; // reset
            validateStep();
        });
    });

    function buildPrendasEstilos(prendaType) {
        elements.prendasEstilosGrid.innerHTML = '';
        let estilos = [];
        if (prendaType === 'Playera') {
            estilos = [
                { name: 'T-Shirt Normal', img: 'https://via.placeholder.com/300x300?text=T-Shirt' },
                { name: 'Polo Hombre', img: 'https://via.placeholder.com/300x300?text=Polo+Hombre' },
                { name: 'Polo Mujer', img: 'https://via.placeholder.com/300x300?text=Polo+Mujer' }
            ];
        } else if (prendaType === 'Sudadera') {
            estilos = [
                { name: 'Sin Bolsa', img: 'sudadera sin bolsas 100% algodon/1.png' },
                { name: 'Con Zipper', img: 'https://via.placeholder.com/300x300?text=Sudadera+Zipper' },
                { name: 'Hoodie con Bolsa', img: 'https://via.placeholder.com/300x300?text=Hoodie' },
                { name: 'Oversize', img: 'https://via.placeholder.com/300x300?text=Oversize' }
            ];
        } else if (prendaType === 'Gorra') {
            estilos = [
                { name: 'Trucker', img: 'https://via.placeholder.com/300x300?text=Gorra+Trucker' },
                { name: 'De Mezclilla', img: 'https://via.placeholder.com/300x300?text=Mezclilla' },
                { name: 'Acrílica', img: 'https://via.placeholder.com/300x300?text=Acrilica' }
            ];
        }

        estilos.forEach(est => {
            const div = document.createElement('div');
            div.className = 'card-option catalog-card';
            div.dataset.value = est.name;
            div.innerHTML = `
                <div class="catalog-img-wrapper">
                    <img src="${est.img}" alt="${est.name}" loading="lazy">
                </div>
                <h3>${est.name}</h3>
            `;
            
            div.addEventListener('click', () => {
                document.querySelectorAll('#prendasEstilosGrid .card-option').forEach(c => c.classList.remove('selected'));
                div.classList.add('selected');
                state.prendas.estilo = est.name;
                validateStep();
            });

            elements.prendasEstilosGrid.appendChild(div);
        });
    }

    elements.tecnicaCards.forEach(card => {
        card.addEventListener('click', () => {
            elements.tecnicaCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            state.prendas.tecnica = card.querySelector('h3').textContent;
            validateStep();
        });
    });

    elements.colorOptions.forEach(opt => {
        opt.addEventListener('click', () => {
            elements.colorOptions.forEach(c => c.classList.remove('selected'));
            opt.classList.add('selected');
            state.prendas.colorBase = opt.dataset.color;
            elements.selectedColorDisplay.textContent = state.prendas.colorBase;
            validateStep();
        });
    });

    elements.qtyInputs.forEach(input => {
        input.addEventListener('input', () => {
            let total = 0;
            elements.qtyInputs.forEach(inp => {
                let val = parseInt(inp.value) || 0;
                if (val < 0) { val = 0; inp.value = 0; }
                state.prendas.cantidades[inp.dataset.size] = val;
                total += val;
            });
            state.prendas.totalQty = total;
            elements.totalQtyDisplay.textContent = total;
            validateStep();
        });
    });

    // --- UNIFORMES INTERACTIONS ---
    elements.uniformeCards.forEach(card => {
        card.addEventListener('click', () => {
            elements.uniformeCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            state.uniformes.prenda = card.dataset.ref;
            state.uniformes.prendaDesc = card.querySelector('h3').textContent + " " + card.dataset.desc;
            state.uniformes.basePrice = parseFloat(card.dataset.price);
            
            // Build dynamic sizes grid
            const isCamisa = state.uniformes.prenda.includes('CAMISA');
            if (isCamisa) {
                elements.uniColorGroup.classList.remove('hidden');
                buildUniSizesGrid(['S', 'M', 'L', 'XL', 'XXL', 'XXXL']);
            } else {
                elements.uniColorGroup.classList.add('hidden');
                buildUniSizesGrid(['28', '30', '32', '34', '36', '38', '40']);
            }
            
            // reset quantities
            state.uniformes.cantidades = {};
            state.uniformes.totalQty = 0;
            elements.uniTotalQtyDisplay.textContent = 0;
            
            validateStep();
        });
    });

    function buildUniSizesGrid(sizes) {
        elements.uniSizesGrid.innerHTML = '';
        sizes.forEach(size => {
            const div = document.createElement('div');
            div.className = 'size-input';
            div.innerHTML = `
                <span>${size}</span>
                <input type="number" min="0" class="uni-qty-input" data-size="${size}" value="0">
            `;
            elements.uniSizesGrid.appendChild(div);
        });

        // Add listeners to new inputs
        document.querySelectorAll('.uni-qty-input').forEach(input => {
            input.addEventListener('input', () => {
                let total = 0;
                document.querySelectorAll('.uni-qty-input').forEach(inp => {
                    let val = parseInt(inp.value) || 0;
                    if (val < 0) { val = 0; inp.value = 0; }
                    state.uniformes.cantidades[inp.dataset.size] = val;
                    total += val;
                });
                state.uniformes.totalQty = total;
                elements.uniTotalQtyDisplay.textContent = total;
                validateStep();
            });
        });
    }

    elements.uniTecnicaCards.forEach(card => {
        card.addEventListener('click', () => {
            elements.uniTecnicaCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            state.uniformes.tecnica = card.querySelector('h3').textContent;
            validateStep();
        });
    });

    elements.uniReflectivoCards.forEach(card => {
        card.addEventListener('click', () => {
            elements.uniReflectivoCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            state.uniformes.reflectivo = card.querySelector('h3').textContent;
            validateStep();
        });
    });

    elements.uniColorOptions.forEach(opt => {
        opt.addEventListener('click', () => {
            elements.uniColorOptions.forEach(c => c.classList.remove('selected'));
            opt.classList.add('selected');
            state.uniformes.colorBase = opt.dataset.color;
            elements.uniSelectedColorDisplay.textContent = state.uniformes.colorBase;
            validateStep();
        });
    });

    // --- GALARDONES INTERACTIONS ---
    elements.galardonesCards.forEach(card => {
        card.addEventListener('click', () => {
            elements.galardonesCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');
            state.galardones.ref = card.dataset.ref;
            state.galardones.desc = card.dataset.desc;
            state.galardones.unitPrice = parseFloat(card.dataset.price);
            validateStep();
        });
    });

    elements.galardonesQty.addEventListener('input', (e) => {
        state.galardones.cantidad = parseInt(e.target.value) || 1;
        validateStep();
    });

    // --- DTF UV INTERACTIONS ---
    elements.dtfQty.addEventListener('input', (e) => {
        state.dtf.metros = parseFloat(e.target.value) || 1;
        validateStep();
    });

    // --- SHARED FILE UPLOAD ---
    elements.browseBtn.addEventListener('click', () => elements.fileInput.click());
    
    elements.dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        elements.dropzone.classList.add('dragover');
    });
    
    elements.dropzone.addEventListener('dragleave', () => {
        elements.dropzone.classList.remove('dragover');
    });
    
    elements.dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        elements.dropzone.classList.remove('dragover');
        if (e.dataTransfer.files.length) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    elements.fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) {
            handleFile(e.target.files[0]);
        }
    });

    elements.removeFileBtn.addEventListener('click', () => {
        state.file = null;
        elements.fileInput.value = '';
        elements.filePreview.classList.add('hidden');
        elements.dropzone.style.display = 'block';
    });

    function handleFile(file) {
        state.file = file;
        elements.fileName.textContent = file.name;
        elements.fileSize.textContent = (file.size / (1024 * 1024)).toFixed(2) + ' MB';
        elements.dropzone.style.display = 'none';
        elements.filePreview.classList.remove('hidden');
    }

    // --- SUMMARY & TOTAL CALCULATION ---
    function calculateTotal() {
        let total = 0;
        if (state.category === 'prendas') {
            if (state.prendas.prenda === 'Playera' && state.prendas.estilo === 'T-Shirt Normal' && state.prendas.totalQty >= 25) {
                for (let [size, qty] of Object.entries(state.prendas.cantidades)) {
                    let price = 50;
                    if (['XL', 'XXL', '3XL'].includes(size)) {
                        price += 10;
                    }
                    total += price * qty;
                }
            } else {
                total = 0; 
            }
        } else if (state.category === 'uniformes') {
            const isCamisa = state.uniformes.prenda && state.uniformes.prenda.includes('CAMISA');
            for(let [size, qty] of Object.entries(state.uniformes.cantidades)) {
                let price = state.uniformes.basePrice;
                if(isCamisa && size === 'XXL') price += 5;
                if(isCamisa && size === 'XXXL') price += 10;
                total += price * qty;
            }
        } else if (state.category === 'galardones') {
            total = state.galardones.unitPrice * state.galardones.cantidad;
        } else if (state.category === 'dtf_uv') {
            total = state.dtf.basePrice * state.dtf.metros;
        }
        state.estimatedTotal = total;
        return total;
    }

    function updateSummary() {
        let html = '';
        calculateTotal();

        if (state.category === 'prendas') {
            html = `
                <div class="summary-row"><span>Categoría:</span><strong>Prendas Personalizadas</strong></div>
                <div class="summary-row"><span>Prenda:</span><strong>${state.prendas.prenda}</strong></div>
                <div class="summary-row"><span>Estilo:</span><strong>${state.prendas.estilo}</strong></div>
                <div class="summary-row"><span>Técnica:</span><strong>${state.prendas.tecnica}</strong></div>
                <div class="summary-row"><span>Color Base:</span><strong>${state.prendas.colorBase}</strong></div>
                <div class="summary-row"><span>Cantidad Total:</span><strong>${state.prendas.totalQty}</strong></div>
            `;
        } else if (state.category === 'uniformes') {
            let sizesStr = Object.entries(state.uniformes.cantidades).filter(([_, qty]) => qty > 0).map(([size, qty]) => `${qty} talla ${size}`).join(', ');
            html = `
                <div class="summary-row"><span>Categoría:</span><strong>Uniformes Industriales</strong></div>
                <div class="summary-row"><span>Prenda:</span><strong>${state.uniformes.prendaDesc}</strong></div>
                <div class="summary-row"><span>Técnica:</span><strong>${state.uniformes.tecnica}</strong></div>
                <div class="summary-row"><span>Cinta Reflectiva:</span><strong>${state.uniformes.reflectivo}</strong></div>
            `;
            if (state.uniformes.colorBase) {
                html += `<div class="summary-row"><span>Color:</span><strong>${state.uniformes.colorBase}</strong></div>`;
            }
            html += `<div class="summary-row"><span>Tallas:</span><strong>${sizesStr} (Total: ${state.uniformes.totalQty})</strong></div>`;
        } else if (state.category === 'galardones') {
            html = `
                <div class="summary-row"><span>Categoría:</span><strong>Galardones de Cristal (DTF UV)</strong></div>
                <div class="summary-row"><span>Modelo Ref:</span><strong>${state.galardones.ref}</strong></div>
                <div class="summary-row"><span>Dimensiones:</span><strong>${state.galardones.desc}</strong></div>
                <div class="summary-row"><span>Precio Unitario:</span><strong>Q ${state.galardones.unitPrice}</strong></div>
                <div class="summary-row"><span>Cantidad:</span><strong>${state.galardones.cantidad}</strong></div>
            `;
        } else if (state.category === 'dtf_uv') {
            html = `
                <div class="summary-row"><span>Categoría:</span><strong>Impresión DTF UV</strong></div>
                <div class="summary-row"><span>Ancho:</span><strong>${state.dtf.ancho}</strong></div>
                <div class="summary-row"><span>Metros:</span><strong>${state.dtf.metros}</strong></div>
            `;
        }

        html += `<div class="summary-row"><span>Diseño Adjunto:</span><strong>${state.file ? state.file.name : 'No adjunto'}</strong></div>`;
        
        let priceText = state.category === 'prendas' && state.estimatedTotal > 0 ? `Q ${state.estimatedTotal.toFixed(2)}` : 'Por confirmar';
        if (state.category !== 'prendas') priceText = `Q ${state.estimatedTotal.toFixed(2)}`;
        
        html += `
            <div class="summary-total">
                <span>Costo Estimado*</span>
                <h3>${priceText}</h3>
                <p class="disclaimer">*Precio referencial. Sujeto a confirmación.</p>
            </div>
        `;
        
        elements.summaryPanelContainer.innerHTML = html;
    }

    // --- SUBMISSION ---
    function validateForm() {
        let valid = true;
        [elements.userName, elements.userPhone, elements.userEmail].forEach(input => {
            if (!input.value.trim()) {
                input.classList.add('input-error');
                valid = false;
            } else {
                input.classList.remove('input-error');
            }
        });
        return valid;
    }

    function generateMessage() {
        let msg = `Hola Mosal, me gustaría cotizar el siguiente pedido:%0A%0A*Detalles del Pedido:*%0A`;
        
        if (state.category === 'prendas') {
            let sizesStr = Object.entries(state.prendas.cantidades).filter(([_, qty]) => qty > 0).map(([size, qty]) => `${qty} talla ${size}`).join(', ');
            msg += `- Categoría: Prendas Personalizadas%0A- Prenda: ${state.prendas.prenda} (${state.prendas.estilo})%0A- Técnica: ${state.prendas.tecnica}%0A- Color Base: ${state.prendas.colorBase}%0A- Cantidades: ${sizesStr} (Total: ${state.prendas.totalQty})%0A`;
        } else if (state.category === 'uniformes') {
            let sizesStr = Object.entries(state.uniformes.cantidades).filter(([_, qty]) => qty > 0).map(([size, qty]) => `${qty} talla ${size}`).join(', ');
            msg += `- Categoría: Uniformes Industriales%0A- Prenda: ${state.uniformes.prendaDesc}%0A- Técnica: ${state.uniformes.tecnica}%0A- Cinta Reflectiva: ${state.uniformes.reflectivo}%0A`;
            if (state.uniformes.colorBase) msg += `- Color: ${state.uniformes.colorBase}%0A`;
            msg += `- Tallas: ${sizesStr} (Total: ${state.uniformes.totalQty})%0A`;
        } else if (state.category === 'galardones') {
            msg += `- Categoría: Galardón de Cristal (DTF UV)%0A- Modelo Ref: ${state.galardones.ref}%0A- Dimensiones: ${state.galardones.desc}%0A- Precio Unitario Referencial: Q ${state.galardones.unitPrice}%0A- Cantidad: ${state.galardones.cantidad}%0A`;
        } else if (state.category === 'dtf_uv') {
            msg += `- Categoría: Impresión DTF UV / Textil%0A- Ancho Máquina: ${state.dtf.ancho}%0A- Metros: ${state.dtf.metros}%0A`;
        }
        
        let priceText = state.category === 'prendas' && state.estimatedTotal > 0 ? `Q ${state.estimatedTotal.toFixed(2)}` : 'Por confirmar';
        if (state.category !== 'prendas') priceText = `Q ${state.estimatedTotal.toFixed(2)}`;
        
        msg += `- Costo Estimado Web: ${priceText}%0A`;
        msg += `- Diseño Adjunto: ${state.file ? 'Sí, lo enviaré por este medio' : 'No'}%0A%0A`;
        
        msg += `*Mis Datos:*%0A- Nombre: ${elements.userName.value}%0A- Teléfono: ${elements.userPhone.value}%0A- Correo: ${elements.userEmail.value}%0A- Notas: ${elements.userNotes.value || 'Ninguna'}%0A`;
        return msg;
    }

    elements.btnWhatsapp.addEventListener('click', () => {
        if (!validateForm()) { alert('Por favor, completa los campos requeridos marcados en rojo.'); return; }
        window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${generateMessage()}`, '_blank');
    });

    elements.btnEmail.addEventListener('click', () => {
        if (!validateForm()) { alert('Por favor, completa los campos requeridos marcados en rojo.'); return; }
        const subject = encodeURIComponent(`Nueva Cotización - ${elements.userName.value}`);
        const body = generateMessage().replace(/%0A/g, '%0D%0A');
        window.location.href = `mailto:cotizaciones@mosal.com?subject=${subject}&body=${body}`;
    });

    updateWizardUI();
});
"""

with open("/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/js/cotizador.js", "w", encoding="utf-8") as f:
    f.write(new_js)

print("Updated JS.")
