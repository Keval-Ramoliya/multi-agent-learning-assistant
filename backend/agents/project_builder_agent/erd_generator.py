from google import genai
client = genai.Client()

def generate_erd(project_desc):
    prompt = f"""
Based on this project:
{project_desc}

Describe an ER diagram in text form.
List:
1) Entities
2) Attributes
3) Relationships

Do NOT generate images.
"""
    return client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    ).text



# def generate_erd_description(message: str) -> str:
#     # TODO: Use LLM to output entities, attributes, and relationships
#     return "Placeholder ER diagram description. (To be implemented)"
