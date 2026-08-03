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
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            # Rename based on page number to easily identify them
            # Page 1: Gorra Mezclilla, Page 2: Gorra Trucker, Page 3: Gorra Acrilica
            # Page 4-7: Sudaderas, Page 8: Polo, Page 9: T-shirt
            # Page 10-13: Size charts
            out_file = os.path.join(out_dir, f"page_{i+1}_img_{img_index}.{ext}")
            with open(out_file, "wb") as f:
                f.write(image_bytes)
            print(f"Extracted {out_file}")
except Exception as e:
    print(f"Error: {e}")
