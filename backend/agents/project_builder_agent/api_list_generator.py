from google import genai
client = genai.Client()

def generate_api_list(project_desc):
    prompt = f"""
Generate a REST API specification for this project.

Return in table format:
METHOD | ENDPOINT | PURPOSE
"""
    return client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    ).text



# def generate_api_list(message: str) -> str:
#     # TODO: Use LLM to list key REST APIs
#     return "Placeholder API endpoints list. (To be implemented)"
