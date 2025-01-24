from pathlib import Path
from PyPDF2 import PdfReader
path = Path(__file__).parent/ "./PasswordProtectPDF/PDFExample.pdf"
with path.open("rb") as f:
    Pdf1 = ((f))
    pdf_reader = PdfReader(Pdf1)
    number_of_pages = len(pdf_reader.pages)

print(f"Numero de Paginas: {number_of_pages}")