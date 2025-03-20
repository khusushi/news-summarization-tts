import streamlit as st
import requests

st.title("News Summarization and Sentiment Analysis")

company = st.text_input("Enter Company Name")

if st.button("Get News & Analysis"):
    response = requests.get(f"http://127.0.0.1:8000/news/?company={company}")
    news_data = response.json()

    st.write("### News Articles")
    for article in news_data["articles"]:
        st.write(f"- {article}")

    st.write("### Sentiment Analysis")
    for article in news_data["articles"]:
        sentiment_response = requests.post("http://127.0.0.1:8000/sentiment/", json={"text": article})
        sentiment = sentiment_response.json()["sentiment"]
        st.write(f"**Sentiment for:** {article[:50]}... -> {sentiment}")

if st.button("Generate Hindi Speech"):
    text = "This is a sample Hindi speech output."
    tts_response = requests.post("http://127.0.0.1:8000/tts/", json={"text": text})
    st.audio(tts_response.json()["audio_file"])
