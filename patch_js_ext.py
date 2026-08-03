import sys

js_path = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/js/cotizador.js"
with open(js_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("page_10_img_0.jpeg", "page_10_img_0.png")
content = content.replace("page_11_img_0.jpeg", "page_11_img_0.png")
content = content.replace("page_12_img_0.jpeg", "page_12_img_0.png")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(content)
