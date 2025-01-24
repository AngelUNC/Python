#24-Enero-2025 Angel Nava 12:52 AM
#Contraseña: pdfpassword
import getpass
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
path = Path(__file__).parent / "./PasswordProtectPDF/PDFExample.pdf"
writer = PdfWriter()
with path.open("rb") as f:
    pdf_reader = PdfReader(f)
    for page in pdf_reader.pages:
        writer.add_page(page)
password = getpass.getpass(f"Establece una Contraseña: ")
writer.encrypt(password)
output_path = Path(__file__).parent / "./PasswordProtectPDF/PDFEncriptado.pdf"
with output_path.open("wb") as output_pdf:
    writer.write(output_pdf)
print(f"Archivo Encriptado Existosamente: {output_path}")