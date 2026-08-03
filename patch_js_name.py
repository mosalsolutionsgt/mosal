import sys

js_path = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/js/cotizador.js"
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

js_content = js_content.replace("if (prendaType === 'Playera')", "if (prendaType === 'Playera / Polo')")
js_content = js_content.replace("if (state.prendas.prenda === 'Playera' && state.prendas.estilo === 'T-Shirt Normal'", "if (state.prendas.prenda === 'Playera / Polo' && state.prendas.estilo === 'T-Shirt Normal'")
js_content = js_content.replace("} else if (state.prendas.prenda === 'Playera' && (state.prendas.estilo === 'Polo Hombre' || state.prendas.estilo === 'Polo Mujer'))", "} else if (state.prendas.prenda === 'Playera / Polo' && (state.prendas.estilo === 'Polo Hombre' || state.prendas.estilo === 'Polo Mujer'))")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
