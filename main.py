from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
from pdf_ingest import ingest_pdf
from rag_service import ask_question
from vector_store import save_index, load_index
from embeddings import generate_embeddings

app = FastAPI()

@app.post("/ingest", status_code=202)
async def ingest(file: UploadFile = File(...)):
    try:
        chunks = await ingest_pdf(file)
        embeddings = generate_embeddings([c["text"] for c in chunks])
        save_index(chunks, embeddings)
        return {"message": "PDF ingested and indexed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask", status_code=200)
async def ask(question: str):
    try:
        response, sources = ask_question(question)
        return JSONResponse(content={"response": response, "sources": sources})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health", status_code=200)
async def health():
    return {"status": "ok"}
