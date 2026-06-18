from fastapi import FastAPI
from pydantic import BaseModel

from ollama import chat

from tools import (
    get_current_time,
    calculator
)

from router import decide_tool

app = FastAPI(
    title="LLM Tool Calling Assistant"
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():

    return {
        "status": "LLM Tool Calling Ready"
    }

@app.post("/chat")
def chat_with_tools(request: ChatRequest):

    # Let the LLM decide which tool to use
    tool = decide_tool(
        request.message
    )

    print(f"Selected Tool: {tool}")

    # Time Tool
    if tool == "time":

        return {
            "tool_used": "time",
            "result": get_current_time()
        }

    # Calculator Tool
    elif tool == "calculator":

        return {
            "tool_used": "calculator",
            "result": calculator(
                request.message
            )
        }

    # Fallback to normal LLM chat
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
        "response": response["message"]["content"]
    }