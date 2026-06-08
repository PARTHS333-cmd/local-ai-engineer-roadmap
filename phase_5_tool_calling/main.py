from fastapi import FastAPI
from pydantic import BaseModel

from tools import (
    get_current_time,
    calculator
)

app = FastAPI(
    title="Tool Calling Assistant"
)

class ToolRequest(BaseModel):
    tool: str
    input: str = ""

@app.get("/")
def home():

    return {
        "status": "Tool Calling Ready"
    }

@app.post("/tool")
def use_tool(request: ToolRequest):

    if request.tool == "time":

        return {
            "result": get_current_time()
        }

    elif request.tool == "calculator":

        return {
            "result":
            calculator(request.input)
        }

    return {
        "error":
        "Tool not found"
    }