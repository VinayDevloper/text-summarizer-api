from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class TextInput(BaseModel):
    text : str
    limit : Optional[int] = None

def ai_summarize(text: str, limit:int):
    words =text.split()
    summary = " ".join(words[:limit])
    return summary

@app.get("/")
def home():
    return{"status": "success","message":"Hi,Vinay Sawant!"}

@app.get("/user/{name}")
def hello_message(name: str):
    return{"status":"success", "msg":f"hari bol {name}"}

@app.post("/summarize")
def summarize(data:TextInput):
    if not data.text.strip():
        return{"status":"error","msg":"Text can not be empty"}
    
    limit = data.limit if data.limit is not None else 20

    summary = ai_summarize(data.text,limit)
    return{"status":"success","summary":summary}

