from fastapi import FastAPI
from pydantic import BaseModel

from ollama import chat

from tools import (
    get_current_time,
    calculator
)

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_with_tools(request: ChatRequest):

    user_message = request.message.lower()

    if "time" in user_message:

        tool_result = get_current_time()

        return {
            "tool_used": "time",
            "result": tool_result
        }

    if any(
        op in user_message
        for op in ["+", "-", "*", "/"]
    ):

        tool_result = calculator(
            user_message
        )

        return {
            "tool_used": "calculator",
            "result": tool_result
        }

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
        "tool_used": None,
        "response":
        response["message"]["content"]
    }