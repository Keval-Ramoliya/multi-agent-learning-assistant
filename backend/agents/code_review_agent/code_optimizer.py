from google import genai

client = genai.Client()

def optimize_code(code: str):
    prompt = f"""
Refactor and optimize this code. Return only the optimized version in a code block.

Code:
"""

    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return res.text