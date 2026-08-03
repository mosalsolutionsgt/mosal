import sys

js_path = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/js/cotizador.js"
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# 1. Add elements for size chart
old_elements = "        qtyInputs: document.querySelectorAll('.qty-input'),"
new_elements = """        qtyInputs: document.querySelectorAll('.qty-input'),
        sizeChartContainer: document.getElementById('sizeChartContainer'),
        sizeChartImg: document.getElementById('sizeChartImg'),"""
js_content = js_content.replace(old_elements, new_elements)

# 2. Update buildPrendasEstilos function
old_build_func = """    function buildPrendasEstilos(prendaType) {
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
    }"""

new_build_func = """    function buildPrendasEstilos(prendaType) {
        elements.prendasEstilosGrid.innerHTML = '';
        let estilos = [];
        if (prendaType === 'Playera') {
            estilos = [
                { name: 'T-Shirt Normal', img: 'assets/mockups/prendas/page_9_img_0.png', chart: 'assets/mockups/prendas/page_13_img_0.png' },
                { name: 'Polo Hombre', img: 'assets/mockups/prendas/page_8_img_0.png', chart: 'assets/mockups/prendas/page_11_img_0.jpeg' },
                { name: 'Polo Mujer', img: 'assets/mockups/prendas/page_8_img_0.png', chart: 'assets/mockups/prendas/page_12_img_0.jpeg' }
            ];
        } else if (prendaType === 'Sudadera') {
            estilos = [
                { name: 'Sin Bolsa', img: 'assets/mockups/prendas/page_4_img_0.png', chart: 'assets/mockups/prendas/page_10_img_0.jpeg' },
                { name: 'Con Zipper', img: 'assets/mockups/prendas/page_5_img_0.png', chart: 'assets/mockups/prendas/page_10_img_0.jpeg' },
                { name: 'Hoodie con Bolsa', img: 'assets/mockups/prendas/page_6_img_0.png', chart: 'assets/mockups/prendas/page_10_img_0.jpeg' },
                { name: 'Oversize', img: 'assets/mockups/prendas/page_7_img_0.png', chart: 'assets/mockups/prendas/page_10_img_0.jpeg' }
            ];
        } else if (prendaType === 'Gorra') {
            estilos = [
                { name: 'Trucker', img: 'assets/mockups/prendas/page_2_img_0.png', chart: null },
                { name: 'De Mezclilla', img: 'assets/mockups/prendas/page_1_img_0.png', chart: null },
                { name: 'Acrílica', img: 'assets/mockups/prendas/page_3_img_0.png', chart: null }
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
                
                // Set Size Chart
                if (est.chart) {
                    elements.sizeChartImg.src = est.chart;
                    elements.sizeChartContainer.style.display = 'block';
                } else {
                    elements.sizeChartContainer.style.display = 'none';
                }

                validateStep();
            });

            elements.prendasEstilosGrid.appendChild(div);
        });
    }"""
js_content = js_content.replace(old_build_func, new_build_func)

# 3. Update calculateTotal
old_calc = """    function calculateTotal() {
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
        } else if (state.category === 'uniformes') {"""

new_calc = """    function calculateTotal() {
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
            } else if (state.prendas.prenda === 'Playera' && (state.prendas.estilo === 'Polo Hombre' || state.prendas.estilo === 'Polo Mujer')) {
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
js_content = js_content.replace(old_calc, new_calc)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("JS Patched.")
