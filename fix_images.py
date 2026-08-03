import fitz
import os

pdf_path = "/Users/herbertmoscoso/.gemini/antigravity-ide/brain/a14c0e7b-f927-44d2-9a5e-ddc49702ebd0/media__1785747485604.pdf"
out_dir = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/mockups/prendas"

os.makedirs(out_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        page = doc[i]
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            
            # Use Pixmap to properly handle alpha/transparency and colorspaces
            pix = fitz.Pixmap(doc, xref)
            
            # If the image has an alpha channel, or is CMYK, we ensure it's converted to standard RGB/RGBA
            if pix.n - pix.alpha < 4:       # this is GRAY or RGB
                pass
            else:                           # CMYK: convert to RGB first
                pix = fitz.Pixmap(fitz.csRGB, pix)
                
            out_file = os.path.join(out_dir, f"page_{i+1}_img_{img_index}.png")
            pix.save(out_file)
            pix = None # free memory
            print(f"Fixed {out_file}")
except Exception as e:
    print(f"Error: {e}")
