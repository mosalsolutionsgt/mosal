import fitz
import os

pdf_path = "/Users/herbertmoscoso/.gemini/antigravity-ide/brain/a14c0e7b-f927-44d2-9a5e-ddc49702ebd0/media__1785775077866.pdf"
out_dir = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/mockups/prendas"

os.makedirs(out_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    
    # Page 1: Polo Mujer
    pix1 = doc[0].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    pix1.save(os.path.join(out_dir, "polo_mujer_chart.png"))
    
    # Page 2: Polo Hombre
    pix2 = doc[1].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    pix2.save(os.path.join(out_dir, "polo_hombre_chart.png"))
    
    print("New Polo charts extracted successfully.")
except Exception as e:
    print(f"Error: {e}")
