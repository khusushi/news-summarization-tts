import requests
from bs4 import BeautifulSoup
import re
from transformers import pipeline
from gtts import gTTS
import os

# ---------------------- NEWS EXTRACTION ----------------------

def extract_news(company_name):
    """Scrape news articles related to the given company from Google search."""
    search_url = f"https://www.google.com/search?q={company_name}+news"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for link in soup.find_all("a", href=True):
        url = link["href"]
        if "http" in url and "google" not in url:
            articles.append(url)
        if len(articles) >= 10:
            break

    return articles

# ---------------------- SENTIMENT ANALYSIS ----------------------

def analyze_sentiment(text):
    """Perform sentiment analysis on a given text."""
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)
    return result[0]["label"]

# ---------------------- TEXT-TO-SPEECH ----------------------

def generate_tts(text, lang="hi", output_file="output.mp3"):
    """Convert text to speech in Hindi and save it as an MP3 file."""
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    return output_file
