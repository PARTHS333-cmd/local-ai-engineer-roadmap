from fastapi import FastAPI
from pydantic import BaseModel

from ollama import chat

from memory import (
    add_message,
    get_history
)

from router import (
    decide_route
)

from rag import (
    search_resume
)

from tools import (
    get_current_time,
    calculator
)

app = FastAPI(
    title="AI Agent"
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():

    return {
        "status": "AI Agent Ready"
    }

@app.get("/history")
def history():

    return get_history()

@app.post("/chat")
def agent_chat(request: ChatRequest):

    user_message = request.message

    add_message(
        "user",
        user_message
    )

    route = decide_route(
        user_message
    )

    print(
        f"Agent Route: {route}"
    )

    # Time Tool
    if route == "time":

        result = get_current_time()

        add_message(
            "assistant",
            result
        )

        return {
            "route": route,
            "response": result
        }

    # Calculator Tool
    elif route == "calculator":

        result = calculator(
            user_message
        )

        add_message(
            "assistant",
            result
        )

        return {
            "route": route,
            "response": result
        }

    # Resume Search
    elif route == "resume_search":

        context = search_resume(
            user_message
        )

        prompt = f"""
Answer using the provided resume context.

Context:
{context}

Question:
{user_message}
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

        answer = (
            response["message"]["content"]
        )

        add_message(
            "assistant",
            answer
        )

        return {
            "route": route,
            "response": answer
        }

    # Normal Chat
    response = chat(
        model="llama3",
        messages=get_history()
    )

    answer = (
        response["message"]["content"]
    )

    add_message(
        "assistant",
        answer
    )

    return {
        "route": "chat",
        "response": answer
    }