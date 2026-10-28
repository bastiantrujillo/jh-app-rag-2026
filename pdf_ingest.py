import os
from PyPDF2 import PdfReader
from config import Config
from utils import chunk_text, save_pdf

async def ingest_pdf(file):
    content = await file.read()
    filename = file.filename or "upload.pdf"
    save_pdf(filename, content)
    pdf_path = os.path.join(Config.PDFS_DIR, filename)
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
    chunks = chunk_text(
        full_text,
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP,
        filename=filename,
        page_num=0
    )
    return chunks
