from fastapi import FastAPI
from pydantic import BaseModel

from memory import (
    initialize_database,
    add_message,
    get_history
)

app = FastAPI(
    title="Production AI Assistant"
)

initialize_database()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():

    return {
        "status": "Production Assistant Ready"
    }

@app.get("/history")
def history():

    return get_history()

@app.post("/chat")
def chat(request: ChatRequest):

    add_message(
        "user",
        request.message
    )

    assistant_response = (
        f"You said: {request.message}"
    )

    add_message(
        "assistant",
        assistant_response
    )

    return {
        "response":
        assistant_response
    }