# Text Summarizer API

A simple FastAPI-based API that summarizes text by returning the first N words.

## 🚀 Features

- Accepts text input  
- Optional word limit  
- Returns summarized text  
- Handles empty input  

## 🛠️ Tech Used

- FastAPI  
- Python  

## ▶️ How to Run

```bash
uvicorn main:app --reload

Then open:

http://127.0.0.1:8000/docs

📥 Example Request
{
  "text": "Learning FastAPI step by step builds strong backend skills over time",
  "limit": 5
}
📤 Example Response
{
  "status": "success",
  "summary": "Learning FastAPI step by step"
}
