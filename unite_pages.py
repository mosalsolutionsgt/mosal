import sys
import os

landing_file = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/gemini-code-1785654406625.html"

with open(landing_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Nav CTA
old_nav = """<a href="https://wa.me/50230292980?text=Hola%2C%20quiero%20cotizar%20un%20pedido%20con%20Mosal%20Solutions" class="btn btn-primary btn-sm nav-cta" target="_blank" rel="noopener">Cotizar por WhatsApp</a>"""
new_nav = """<a href="cotizador.html" class="btn btn-primary btn-sm nav-cta">Cotizador en Línea</a>"""
content = content.replace(old_nav, new_nav)

# Replace Hero CTA
old_hero = """        <a href="https://wa.me/50230292980?text=Hola%2C%20quiero%20cotizar%20un%20pedido%20con%20Mosal%20Solutions" class="btn btn-primary btn-lg" target="_blank" rel="noopener">
          Cotizar por WhatsApp
        </a>"""
new_hero = """        <a href="cotizador.html" class="btn btn-primary btn-lg">
          Abrir Cotizador en Línea
        </a>"""
content = content.replace(old_hero, new_hero)

# Replace Footer CTA
old_footer = """      <a href="https://wa.me/50230292980?text=Hola%2C%20tengo%20una%20idea%20que%20quiero%20convertir%20en%20pieza" class="btn btn-primary btn-lg" target="_blank" rel="noopener">
        Contáctanos ahora
      </a>"""
new_footer = """      <a href="cotizador.html" class="btn btn-primary btn-lg">
        Abrir Cotizador
      </a>"""
content = content.replace(old_footer, new_footer)

with open(landing_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Landing page patched.")
