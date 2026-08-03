import sys

html_path = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/cotizador.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add categories
old_categories = """                <div class="card-option category-card" data-category="dtf_uv">
                    <span class="card-icon">📏</span>
                    <h3>Metros de DTF UV</h3>
                </div>
            </div>"""

new_categories = """                <div class="card-option category-card" data-category="dtf_uv">
                    <span class="card-icon">📏</span>
                    <h3>Metros de DTF UV</h3>
                </div>
                <div class="card-option category-card" data-category="stickers">
                    <span class="card-icon">🏷️</span>
                    <h3>Stickers</h3>
                </div>
                <div class="card-option category-card" data-category="otros">
                    <span class="card-icon">📦</span>
                    <h3>Otros Productos</h3>
                </div>
            </div>"""
content = content.replace(old_categories, new_categories)

# 2. Add Tamaño de Diseño
old_tecnica = """                    <div class="form-group">
                        <label>Técnica de Personalización</label>
                        <div class="cards-grid" id="tecnicaCards">"""

new_tecnica = """                    <div class="form-group">
                        <label>Técnica de Personalización</label>
                        <div class="cards-grid" id="tecnicaCards">"""

old_end_tecnica = """                            <div class="card-option" data-value="sublimacion" data-tech-price="0">
                                <span class="card-icon">🎨</span>
                                <h3>Sublimación</h3>
                            </div>
                        </div>
                    </div>
                </section>"""

new_end_tecnica = """                            <div class="card-option" data-value="sublimacion" data-tech-price="0">
                                <span class="card-icon">🎨</span>
                                <h3>Sublimación</h3>
                            </div>
                        </div>
                    </div>

                    <div class="form-group" id="tamanoDisenoGroup" style="display: none; margin-top: 25px;">
                        <label>Tamaño del Diseño</label>
                        <div class="cards-grid" id="tamanoDisenoCards">
                            <div class="card-option" data-value="10 cm">
                                <span class="card-icon" style="font-size: 1.5rem;">📏</span>
                                <h3>10 cm<br><small style="color:var(--text-muted); font-size: 0.75rem;">Logo Pequeño</small></h3>
                            </div>
                            <div class="card-option" data-value="15 - 20 cm">
                                <span class="card-icon" style="font-size: 1.5rem;">📐</span>
                                <h3>15 - 20 cm<br><small style="color:var(--text-muted); font-size: 0.75rem;">Mediano</small></h3>
                            </div>
                            <div class="card-option" data-value="25 cm">
                                <span class="card-icon" style="font-size: 1.5rem;">🖼️</span>
                                <h3>25 cm<br><small style="color:var(--text-muted); font-size: 0.75rem;">Grande</small></h3>
                            </div>
                        </div>
                    </div>
                </section>"""
content = content.replace(old_end_tecnica, new_end_tecnica)

# 3. Add Stickers and Otros Productos sections before Contact Step
old_contact = """                <!-- Paso 6: Resumen -->"""

new_contact = """                <!-- Paso de Stickers -->
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

                <!-- Paso 6: Resumen -->"""
content = content.replace(old_contact, new_contact)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML Patched.")
