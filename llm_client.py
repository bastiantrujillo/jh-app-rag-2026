import requests
from config import Config

def call_llm(question, context):
    prompt = f"Context: {context}\nQuestion: {question}"
    payload = {
        "model": "qwen-14b",
        "messages": [
            {"role": "system", "content": "Responde únicamente con base en el contexto recuperado de los documentos. Si la respuesta no aparece en el contexto, di claramente que no está en los documentos proporcionados. No inventes información. Cuando sea posible, menciona la fuente usando nombre de archivo y página."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 700
    }
    response = requests.post(f"{Config.LLM_ENDPOINT}{Config.LLM_CHAT_ENDPOINT}", json=payload)
    data = response.json()
    return data["choices"][0]["message"]["content"], []
