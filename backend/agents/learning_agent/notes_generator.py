# backend/agents/learning_agent/notes_generator.py
from google import genai
from backend.config.settings import GENAI_API_KEY

client = genai.Client()

def generate_notes(message: str):
    prompt = f"""
Create short, exam-friendly notes (bulleted) for the following topic:

{message}

Limit to 200-300 words.
"""
    res = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return res.text
