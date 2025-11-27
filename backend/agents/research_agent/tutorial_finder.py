from google import genai
client = genai.Client()

def find_tutorials(topic: str):
    prompt = f"""
Find best tutorials for learning {topic}.
Return a clean list: Link + Summary.
"""
    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return res.text
