from fastapi import FastAPI
from pydantic import BaseModel
from ollama import chat

app = FastAPI(
    title="Local AI Assistant",
    version="2.0"
)

conversation_history = []

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "status": "running",
        "memory_enabled": True
    }

@app.post("/chat")
def chat_with_ai(request: ChatRequest):

    conversation_history.append(
        {
            "role": "user",
            "content": request.message
        }
    )

    response = chat(
        model="llama3",
        messages=conversation_history
    )

    ai_message = response["message"]["content"]

    conversation_history.append(
        {
            "role": "assistant",
            "content": ai_message
        }
    )

    return {
        "response": ai_message,
        "history_length": len(conversation_history)
    }