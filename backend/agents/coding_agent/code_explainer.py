from google import genai
from dotenv import load_dotenv
import os


load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
# print(client)


def explain_code(message: str):
    prompt = f"""
You are a senior coding tutor.
Explain this code in simple detailed steps:

{message}

Your output must follow this structure:
1. Summary
2. Line-by-line explanation
3. Time Complexity
4. Space Complexity
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text



# def explain_code(message: str) -> str:
#     # TODO: Integrate with LLM/ADK
#     return "This is a placeholder explanation for the provided code. (To be implemented)"
