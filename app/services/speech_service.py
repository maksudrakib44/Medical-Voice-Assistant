import os
import streamlit as st
from groq import Groq

class SpeechService:
    def __init__(self):
        self.client = Groq(api_key=st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY"))

    def transcribe(self, file_path: str) -> str:
        """Transcribe audio using Groq's Whisper API"""
        with open(file_path, "rb") as audio_file:
            transcript = self.client.audio.transcriptions.create(
                model="whisper-large-v3-turbo",
                file=audio_file,
            )
        return transcript.text