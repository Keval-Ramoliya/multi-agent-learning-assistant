from google import genai
client = genai.Client()

def stackoverflow_style_answer(topic: str):
    prompt = f"""
Give a StackOverflow-style explanation for:
{topic}
"""
    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return res.text
