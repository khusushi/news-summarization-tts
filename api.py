from fastapi import FastAPI
from pydantic import BaseModel
from utils import extract_news  # Ensure utils.py exists

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to the News Summarization API"}
class CompanyInput(BaseModel):
    company_name: str

@app.post("/get-news/")
def get_news(input: CompanyInput):
    news_data = extract_news(input.company_name)
    return {"company": input.company_name, "articles": news_data}
