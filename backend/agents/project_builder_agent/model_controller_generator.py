from google import genai
client = genai.Client()

def generate_models_controllers(project_desc):
    prompt = f"""
For this project:
{project_desc}

List:
1) All required Backend Models
2) All Controllers & what they handle
"""
    return client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    ).text


# def generate_models_and_controllers_plan(message: str) -> str:
#     # TODO: Use LLM to plan models/controllers structure (for Laravel, Flask, etc.)
#     return "Placeholder models & controllers design. (To be implemented)"
