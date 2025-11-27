from google import genai
client = genai.Client()

def generate_step_plan(project_desc):
    prompt = f"""
Create a step-by-step implementation plan for the project:

{project_desc}

Include:
- Step 1: Database setup
- Step 2: Backend setup
- Step 3: API implementation
- Step 4: Frontend integration
- Step 5: Testing plan (unit + integration)

Format in numbered steps.
"""
    return client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    ).text


# def generate_step_by_step_plan(message: str) -> str:
#     # TODO: Use LLM to generate implementation + test plan
#     return "Placeholder step-by-step and test plan. (To be implemented)"
