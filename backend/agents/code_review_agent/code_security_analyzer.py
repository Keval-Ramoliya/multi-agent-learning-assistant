from google import genai

client = genai.Client()

def analyze_security(code: str):
    prompt = f"""
Analyze security vulnerabilities in this code.

Return:
- Vulnerabilities
- Severity
- Fix recommendations

Code:
"""

    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return res.text
