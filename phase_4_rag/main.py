from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

from ollama import chat

app = FastAPI(
    title="Resume RAG Assistant"
)

embedding = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {
        "status": "RAG Ready"
    }

@app.post("/ask")
def ask_question(request: QuestionRequest):

    docs = vectorstore.similarity_search(
        request.question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Use the provided context to answer.

Context:
{context}

Question:
{request.question}
"""

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    retrieved_chunks = [
    doc.page_content[:300]
    for doc in docs
    ]


    return {
        "question": request.question,
        "answer": response["message"]["content"],
        "sources_found": len(docs),
        "retrieved_chunks": retrieved_chunks
    }
