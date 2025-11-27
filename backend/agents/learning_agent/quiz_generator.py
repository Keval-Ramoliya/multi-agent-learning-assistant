# backend/agents/learning_agent/quiz_generator.py
from google import genai
from backend.config.settings import GENAI_API_KEY

client = genai.Client()

def generate_quiz(message: str):
    prompt = f"""
Generate a 5-question quiz for the topic below.
For each question, provide:
- Question
- 4 options (A,B,C,D)
- Correct option
- Short explanation (1-2 lines)

Topic:
{message}
"""
    res = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return res.text



# def generate_quiz(message: str) -> str:
#     # TODO: Integrate with LLM/ADK
#     return "Placeholder quiz questions for this topic. (To be implemented)"
