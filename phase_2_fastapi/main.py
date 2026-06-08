from fastapi import FastAPI
from pydantic import BaseModel
from ollama import chat

app = FastAPI(
    title="Local AI Assistant",
    description="FastAPI + Ollama + Llama3",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "status": "running",
        "model": "llama3"
    }

@app.post("/chat")
def chat_with_ai(request: ChatRequest):

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    return {
        "user_message": request.message,
        "ai_response": response["message"]["content"]
    }