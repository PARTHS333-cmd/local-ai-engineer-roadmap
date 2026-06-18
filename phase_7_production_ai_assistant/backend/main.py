from fastapi import FastAPI
from pydantic import BaseModel

from ollama import chat

from memory import (
    initialize_database,
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
def assistant_chat(request: ChatRequest):

    user_message = request.message

    add_message(
        "user",
        user_message
    )

    route = decide_route(
        user_message
    )

    print(f"Route Selected: {route}")

    # -------------------------
    # TIME TOOL
    # -------------------------

    if route == "time":

        response_text = get_current_time()

        add_message(
            "assistant",
            response_text
        )

        return {
            "route": route,
            "response": response_text
        }

    # -------------------------
    # CALCULATOR TOOL
    # -------------------------

    elif route == "calculator":

        response_text = calculator(
            user_message
        )

        add_message(
            "assistant",
            response_text
        )

        return {
            "route": route,
            "response": response_text
        }

    # -------------------------
    # RAG SEARCH
    # -------------------------

    elif route == "resume_search":

        context = search_resume(
            user_message
        )

        prompt = f"""
You are an AI assistant.

Answer ONLY using the provided context.

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

        response_text = (
            response["message"]["content"]
        )

        add_message(
            "assistant",
            response_text
        )

        return {
            "route": route,
            "response": response_text
        }

    # -------------------------
    # NORMAL CHAT WITH MEMORY
    # -------------------------

    history = get_history()

    response = chat(
        model="llama3",
        messages=history
    )

    response_text = (
        response["message"]["content"]
    )

    add_message(
        "assistant",
        response_text
    )

    return {
        "route": "chat",
        "response": response_text
    }