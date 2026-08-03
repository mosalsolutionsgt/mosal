import fitz
import os

pdf_path = "/Users/herbertmoscoso/.gemini/antigravity-ide/brain/a14c0e7b-f927-44d2-9a5e-ddc49702ebd0/media__1785743529638.pdf"
output_dir = "/Users/herbertmoscoso/Downloads/WEB MOSAL FINAL/assets/mockups/uniformes_temp"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)

for page_index in range(len(doc)):
    page = doc[page_index]
    image_list = page.get_images(full=True)
    
    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        image_name = f"page_{page_index+1}_img_{image_index}.{image_ext}"
        with open(os.path.join(output_dir, image_name), "wb") as f:
            f.write(image_bytes)

print(f"Extracted all images to {output_dir}")
