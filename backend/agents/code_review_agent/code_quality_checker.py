from google import genai

client = genai.Client()

def analyze_quality(code: str):
    prompt = f"""
Analyze this code and return:

1. Summary of the code
2. Issues found
3. Line-by-line review

Code:

"""

    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return {
        "summary": res.text,
        "issues": res.text,
        "line_review": res.text
    }
