import numpy as np
from vector_store import load_index
from embeddings import generate_embeddings
from llm_client import call_llm
from config import Config

def ask_question(question):
    index, chunks = load_index()
    if index is None or chunks is None:
        return "No indexed data found.", []
    question_embedding = generate_embeddings([question])
    if not question_embedding:
        return "Failed to generate embedding.", []
    q_emb = np.array(question_embedding[0], dtype=np.float32).reshape(1, -1)
    D, I = index.search(q_emb, Config.TOP_K)
    sources = []
    context_chunks = []
    for idx in I[0]:
        if 0 <= idx < len(chunks):
            chunk_data = chunks[idx]
            if isinstance(chunk_data, dict):
                context_chunks.append(chunk_data.get("text", str(chunk_data)))
                sources.append(chunk_data.get("filename", "unknown"))
            else:
                context_chunks.append(str(chunk_data))
    context = "\n".join(context_chunks)
    response, srcs = call_llm(question, context)
    return response, sources if sources else srcs
