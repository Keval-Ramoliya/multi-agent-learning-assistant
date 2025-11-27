from google import genai
client = genai.Client()

def debug_code(message: str):
    prompt = f"""
You are an expert debugger.
The user has a code error. Identify the issue and provide the corrected code.

User Message:
{message}

Output Format:
1. Error Explanation
2. Correct Code
3. Why this fix works
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text




# def debug_code_error(message: str) -> str:
#     # TODO: Integrate with LLM/ADK
#     return "This is a placeholder debug analysis of your error. (To be implemented)"
