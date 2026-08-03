import fitz
import os

pdf_path = "/Users/herbertmoscoso/.gemini/antigravity-ide/brain/a14c0e7b-f927-44d2-9a5e-ddc49702ebd0/media__1785747485604.pdf"
out_dir = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/mockups/prendas"

os.makedirs(out_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        page = doc[i]
        
        rect = page.rect
        width = rect.width
        height = rect.height
        
        # Crop logic
        if i < 9:
            # Crop top 20% and bottom 25%
            clip = fitz.Rect(0, height * 0.20, width, height * 0.75)
        else:
            clip = rect
            
        zoom = 2.0
        mat = fitz.Matrix(zoom, zoom)
        
        pix = page.get_pixmap(matrix=mat, clip=clip, alpha=False)
        out_file = os.path.join(out_dir, f"page_{i+1}_img_0.png")
        pix.save(out_file)
        
        print(f"Rendered {out_file}")
except Exception as e:
    print(f"Error: {e}")
