import sys

html_path = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/cotizador.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """                <section class="wizard-step flow-prendas" id="step_prendas_3" data-step-id="3">
                    <h2>3. Detalles y Cantidades</h2>"""

replacement = """                <section class="wizard-step flow-prendas" id="step_prendas_3" data-step-id="3">
                    <h2>3. Detalles y Cantidades</h2>
                    
                    <!-- Contenedor dinámico de Tabla de Tallas -->
                    <div id="sizeChartContainer" style="display: none; margin-bottom: 20px; text-align: center;">
                        <img id="sizeChartImg" src="" alt="Tabla de Tallas" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    </div>"""

content = content.replace(target, replacement)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML Patched.")
