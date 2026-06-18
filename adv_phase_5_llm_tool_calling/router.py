from ollama import chat

def decide_tool(user_message):

    prompt = f"""
You are a tool routing assistant.

Available tools:

time
calculator
resume_search
chat

Rules:

- If the user asks for the current time, return:
time

- If the user asks for a mathematical calculation, return:
calculator

- Otherwise return:
none

User:
{user_message}

Return only one word.
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

    return (
        response["message"]["content"]
        .strip()
        .lower()
    )