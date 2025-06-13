from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    issueKey: int

@app.post("/createIssue/{issueKey}")
def add_numbers(issueKey: int):
    return {"result = ": issueKey}
