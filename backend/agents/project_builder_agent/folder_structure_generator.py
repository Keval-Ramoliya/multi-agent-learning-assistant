from google import genai
client = genai.Client()

def generate_folder_structure(project_desc):
    prompt = f"""
Generate a clean and realistic folder structure for this project:

{project_desc}

Return as a code block.
"""
    return client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    ).text


# def generate_folder_structure(message: str) -> str:
#     # TODO: Use LLM/ADK to design project-specific folder structures
#     return "Placeholder folder structure for the described project. (To be implemented)"
