import sys

html_path = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/cotizador.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacement 1: step_prendas_1 and creating step_prendas_2
old_step_1 = """                <section class="wizard-step flow-prendas" id="step_prendas_1" data-step-id="1">
                    <h2>1. ¿Qué deseas personalizar?</h2>
                    
                    <div class="form-group">
                        <label>Tipo de Prenda</label>
                        <div class="cards-grid" id="prendaCards">
                            <div class="card-option" data-value="playera" data-base-price="0">
                                <span class="card-icon">👕</span>
                                <h3>Playera</h3>
                            </div>
                            <div class="card-option" data-value="sudadera" data-base-price="0">
                                <span class="card-icon">🧥</span>
                                <h3>Sudadera</h3>
                            </div>
                            <div class="card-option" data-value="gorra" data-base-price="0">
                                <span class="card-icon">🧢</span>
                                <h3>Gorra</h3>
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Técnica de Personalización</label>
                        <div class="cards-grid" id="tecnicaCards">
                            <div class="card-option" data-value="dtf" data-tech-price="0">
                                <span class="card-icon">🖨️</span>
                                <h3>DTF</h3>
                                <p class="tooltip">Impresión digital de alta calidad.</p>
                            </div>
                            <div class="card-option" data-value="vinil_textil" data-tech-price="0">
                                <span class="card-icon">✂️</span>
                                <h3>Vinil Textil</h3>
                                <p class="tooltip">Acabado liso, ideal para logotipos sólidos.</p>
                            </div>
                            <div class="card-option" data-value="bordado" data-tech-price="0">
                                <span class="card-icon">🧵</span>
                                <h3>Bordado</h3>
                                <p class="tooltip">Elegante, duradero y profesional.</p>
                            </div>
                            <div class="card-option" data-value="sublimacion" data-tech-price="0">
                                <span class="card-icon">🎨</span>
                                <h3>Sublimación</h3>
                                <p class="tooltip">Tacto cero, ideal para poliéster blanco.</p>
                            </div>
                        </div>
                    </div>
                </section>"""

new_step_1_2 = """                <section class="wizard-step flow-prendas" id="step_prendas_1" data-step-id="1">
                    <h2>1. ¿Qué tipo de prenda buscas?</h2>
                    
                    <div class="form-group">
                        <div class="cards-grid" id="prendaCards">
                            <div class="card-option" data-value="playera" data-base-price="0">
                                <span class="card-icon">👕</span>
                                <h3>Playera</h3>
                            </div>
                            <div class="card-option" data-value="sudadera" data-base-price="0">
                                <span class="card-icon">🧥</span>
                                <h3>Sudadera</h3>
                            </div>
                            <div class="card-option" data-value="gorra" data-base-price="0">
                                <span class="card-icon">🧢</span>
                                <h3>Gorra</h3>
                            </div>
                        </div>
                    </div>
                </section>

                <section class="wizard-step flow-prendas" id="step_prendas_2" data-step-id="2">
                    <h2>2. Selecciona tu Estilo y Técnica</h2>
                    
                    <div class="form-group">
                        <label>Estilo de Prenda</label>
                        <div class="cards-grid" id="prendasEstilosGrid">
                            <!-- Inyectado via JS -->
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Técnica de Personalización</label>
                        <div class="cards-grid" id="tecnicaCards">
                            <div class="card-option" data-value="dtf" data-tech-price="0">
                                <span class="card-icon">🖨️</span>
                                <h3>DTF</h3>
                            </div>
                            <div class="card-option" data-value="vinil_textil" data-tech-price="0">
                                <span class="card-icon">✂️</span>
                                <h3>Vinil Textil</h3>
                            </div>
                            <div class="card-option" data-value="bordado" data-tech-price="0">
                                <span class="card-icon">🧵</span>
                                <h3>Bordado</h3>
                            </div>
                            <div class="card-option" data-value="sublimacion" data-tech-price="0">
                                <span class="card-icon">🎨</span>
                                <h3>Sublimación</h3>
                            </div>
                        </div>
                    </div>
                </section>"""

content = content.replace(old_step_1, new_step_1_2)

# Replacement 2: old step_prendas_2 -> step_prendas_3
old_step_2_to_3 = """<section class="wizard-step flow-prendas" id="step_prendas_2" data-step-id="2">
                    <h2>2. Detalles y Cantidades</h2>"""

new_step_2_to_3 = """<section class="wizard-step flow-prendas" id="step_prendas_3" data-step-id="3">
                    <h2>3. Detalles y Cantidades</h2>"""
content = content.replace(old_step_2_to_3, new_step_2_to_3)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated HTML.")
