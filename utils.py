import os

def save_pdf(filename, content):
    os.makedirs("app/data/pdfs", exist_ok=True)
    pdf_path = os.path.join("app/data/pdfs", filename)
    with open(pdf_path, "wb") as f:
        f.write(content)
    return pdf_path

def chunk_text(text, chunk_size, chunk_overlap, filename, page_num):
    if chunk_size <= chunk_overlap:
        chunk_overlap = chunk_size // 2
    chunks = []
    step = max(1, chunk_size - chunk_overlap)
    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]
        chunks.append({
            "text": chunk,
            "filename": filename,
            "page_num": page_num,
            "chunk_id": i // step
        })
    return chunks
