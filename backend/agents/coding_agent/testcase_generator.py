from google import genai
client = genai.Client()

def generate_testcases(message: str):
    prompt = f"""
Generate 5 detailed test cases for the following code/problem:

{message}

Format each test case like:
- Input:
- Expected Output:
- Explanation:
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text





# def generate_test_cases_and_complexity(message: str) -> str:
#     # TODO: Integrate with LLM/ADK
#     return "Here are placeholder test cases and time/space complexity. (To be implemented)"
