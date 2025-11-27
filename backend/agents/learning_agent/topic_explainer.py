# backend/agents/learning_agent/topic_explainer.py
from google import genai
from backend.config.settings import GENAI_API_KEY

client = genai.Client()

def explain_topic(message: str):
    prompt = f"""
You are a patient teacher. Teach the following topic in a structured way with examples.

Topic request:
{message}

Structure:
1) Short overview (2-3 sentences)
2) Key concepts (bulleted)
3) Step-by-step explanation with simple examples
4) 3 practice questions with answers

Keep it concise and student-friendly.
"""
    res = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return res.text


# def explain_topic(message: str) -> str:
#     # TODO: Integrate with LLM/ADK
#     return "Placeholder explanation for the requested topic. (To be implemented)"
