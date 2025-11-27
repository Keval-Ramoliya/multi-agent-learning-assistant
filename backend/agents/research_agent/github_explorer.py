from google import genai
client = genai.Client()

def find_github_repos(topic: str):
    prompt = f"""
Find top GitHub repositories for: {topic}.
Return format:
- Repo Name
- Link
- Stars
- Why it's useful
"""
    res = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return res.text
