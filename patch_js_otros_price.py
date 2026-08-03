import sys

js_path = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/js/cotizador.js"
with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update updateSummary
old_summary_price = """        let priceText = state.category === 'prendas' && state.estimatedTotal > 0 ? `Q ${state.estimatedTotal.toFixed(2)}` : 'Por confirmar';
        if (state.category !== 'prendas') priceText = `Q ${state.estimatedTotal.toFixed(2)}`;
        
        html += `
            <div class="summary-total">
                <span>Costo Estimado*</span>
                <h3>${priceText}</h3>
                <p class="disclaimer">*Precio referencial. Sujeto a confirmación.</p>
            </div>
        `;"""

new_summary_price = """        let priceText = state.category === 'prendas' && state.estimatedTotal > 0 ? `Q ${state.estimatedTotal.toFixed(2)}` : 'Por confirmar';
        if (state.category !== 'prendas') priceText = `Q ${state.estimatedTotal.toFixed(2)}`;
        
        if (state.category !== 'otros') {
            html += `
                <div class="summary-total">
                    <span>Costo Estimado*</span>
                    <h3>${priceText}</h3>
                    <p class="disclaimer">*Precio referencial. Sujeto a confirmación.</p>
                </div>
            `;
        } else {
            html += `
                <div class="summary-total" style="background: transparent; border: none; box-shadow: none;">
                    <span style="color: var(--text-main); font-size: 1rem;">Sujeto a confirmación de inventario y diseño.</span>
                </div>
            `;
        }"""
content = content.replace(old_summary_price, new_summary_price)

# Update generateMessage
old_msg_price = """        let priceText = state.category === 'prendas' && state.estimatedTotal > 0 ? `Q ${state.estimatedTotal.toFixed(2)}` : 'Por confirmar';
        if (state.category !== 'prendas') priceText = `Q ${state.estimatedTotal.toFixed(2)}`;
        
        msg += `- Costo Estimado Web: ${priceText}%0A`;"""

new_msg_price = """        let priceText = state.category === 'prendas' && state.estimatedTotal > 0 ? `Q ${state.estimatedTotal.toFixed(2)}` : 'Por confirmar';
        if (state.category !== 'prendas') priceText = `Q ${state.estimatedTotal.toFixed(2)}`;
        
        if (state.category !== 'otros') {
            msg += `- Costo Estimado Web: ${priceText}%0A`;
        } else {
            msg += `- Costo Estimado Web: Pendiente de confirmación de inventario%0A`;
        }"""
content = content.replace(old_msg_price, new_msg_price)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("JS Patched for Otros Productos Price.")
