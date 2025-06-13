from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    issueKey: str

@app.post("/createIssue")
def add_numbers(issueKey: str):
    return {"result = ": issueKey}
