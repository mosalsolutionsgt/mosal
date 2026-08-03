import sys

html_path = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/cotizador.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """                <!-- ============================ -->
                <!-- PASOS COMPARTIDOS -->
                <!-- ============================ -->
                <!-- STEP 3: Diseño (Aplica para todos) -->"""

replacement = """                <!-- Paso de Stickers -->
                <section class="wizard-step flow-stickers" id="step_stickers_1" data-step-id="1">
                    <h2>1. Cotización de Stickers</h2>
                    <p class="step-subtitle">Los precios mostrados son por cada ciento (100 unidades).</p>
                    <div class="form-group">
                        <label>Medida (cm)</label>
                        <select id="stickerSize" style="width: 100%; padding: 12px; background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); color: white; border-radius: var(--radius-sm);">
                            <option value="" disabled selected>Selecciona una medida</option>
                            <option value="3x3" data-price="35">3 x 3 cm - Q35</option>
                            <option value="4x4" data-price="40">4 x 4 cm - Q40</option>
                            <option value="5x5" data-price="60">5 x 5 cm - Q60</option>
                            <option value="6x6" data-price="90">6 x 6 cm - Q90</option>
                            <option value="7x7" data-price="120">7 x 7 cm - Q120</option>
                            <option value="8x8" data-price="150">8 x 8 cm - Q150</option>
                            <option value="9x9" data-price="186">9 x 9 cm - Q186</option>
                            <option value="10x10" data-price="215">10 x 10 cm - Q215</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Cantidad (en Cientos)</label>
                        <p class="step-subtitle">Ej. 2 = 200 stickers</p>
                        <input type="number" id="stickerQty" min="1" value="1" style="width: 100%; padding: 12px; background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); color: white; border-radius: var(--radius-sm);">
                    </div>
                </section>

                <!-- Paso de Otros Productos -->
                <section class="wizard-step flow-otros" id="step_otros_1" data-step-id="1">
                    <h2>1. ¿Qué estás buscando?</h2>
                    <p class="step-subtitle">Déjanos saber qué otro producto te interesa (ej. pachones, tazas, libretas, lapiceros) y cantidades aproximadas. Si cuentas con el diseño, adjúntalo en el siguiente paso.</p>
                    <div class="form-group">
                        <textarea id="otrosText" rows="5" style="width: 100%; padding: 12px; background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); color: white; border-radius: var(--radius-sm); resize: vertical;" placeholder="Describe tu necesidad aquí..."></textarea>
                    </div>
                </section>

                <!-- ============================ -->
                <!-- PASOS COMPARTIDOS -->
                <!-- ============================ -->
                <!-- STEP 3: Diseño (Aplica para todos) -->"""
content = content.replace(target, replacement)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML Missing Steps Patched.")
