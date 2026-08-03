import fitz
import sys

pdf_path = "sudadera sin bolsas 100% algodon.pdf"

try:
    doc = fitz.open(pdf_path)
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text()
        print(f"--- PAGE {i+1} ---")
        print(text.strip())
        print("="*40)
except Exception as e:
    print(f"Error: {e}")
