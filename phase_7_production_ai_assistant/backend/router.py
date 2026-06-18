from ollama import chat

def decide_route(user_message):

    prompt = f"""
You are an AI routing assistant.

Available routes:

time
calculator
resume_search
chat

Rules:

- Questions about current time → time

- Mathematical expressions → calculator

- Questions about resume, projects,
skills, education, experience → resume_search

- Everything else → chat

User:
{user_message}

Return only one route.
"""

    response = chat(
        model="llama3",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return (
        response["message"]["content"]
        .strip()
        .lower()
    )