from google import genai
client = genai.Client()

def create_quiz(text: str):
    prompt = f"""
Create 5 MCQ questions based on this text:

{text}
"""
    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return res.text
