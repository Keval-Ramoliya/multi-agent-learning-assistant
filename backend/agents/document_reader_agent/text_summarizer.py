from google import genai
client = genai.Client()

def summarize_text(text: str):
    prompt = f"""
Summarize the following text into clean notes:

{text}
"""
    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return res.text
