# backend/agents/learning_agent/mindmap_generator.py
from google import genai
from backend.config.settings import GENAI_API_KEY

client = genai.Client()

def generate_mindmap(message: str):
    prompt = f"""
Create a text-based mindmap for the topic below using nested bullets:

{message}

Example:
Topic
  - Subtopic 1
    - Point A
    - Point B
  - Subtopic 2
"""
    res = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return res.text






# def generate_mindmap(message: str) -> str:
#     # TODO: Create a text-based mind map outline here using LLM
#     return "Placeholder text-based mind map for this topic. (To be implemented)"
