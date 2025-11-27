# backend/agents/project_builder_agent/project_agent.py
from google import genai
from backend.config.settings import GENAI_API_KEY

# Import sub-modules
from .folder_structure_generator import generate_folder_structure
from .erd_generator import generate_erd
from .api_list_generator import generate_api_list
from .model_controller_generator import generate_models_controllers
from .project_planner import generate_step_plan

client = genai.Client(api_key=GENAI_API_KEY)

def handle_project_task(message: str, intent: str = "plan"):
    """
    Full enhanced Project Builder Agent (Day 3 version).
    Generates: folder structure, ERD, APIs, models/controllers, step-by-step plan, and test plan.
    """

    project_desc = message.strip()

    # 1) Folder Structure
    folder_struct = generate_folder_structure(project_desc)

    # 2) ERD (Text-based)
    erd_desc = generate_erd(project_desc)

    # 3) API List
    api_list = generate_api_list(project_desc)

    # 4) Models + Controllers
    models_ctrl = generate_models_controllers(project_desc)

    # 5) Step-by-Step Plan (includes test plan inside)
    step_plan = generate_step_plan(project_desc)

    # Final formatted response
    return f"""
# 🧱 Project Blueprint: {project_desc}

## 1️⃣ Short Summary
This section explains the project in simple words and sets expectations for the rest of the blueprint.

## 2️⃣ Suggested Tech Stack
- Backend: Python (Flask or FastAPI)
- Frontend: HTML/CSS/JS or React (optional)
- Database: MySQL
- ORM: SQLAlchemy
- AI Layer: Gemini + ADK
- Authentication: JWT (optional)
- Deployment: Render / Heroku / Railway (optional)

---

## 3️⃣ 📂 Folder Structure
{folder_struct}

---

## 4️⃣ 🔷 ER Diagram (Text Description)
{erd_desc}

---

## 5️⃣ 🔌 REST API List
{api_list}

---

## 6️⃣ 🧩 Models & Controllers
{models_ctrl}

---

## 7️⃣ 🛠 Step-by-Step Implementation Plan
{step_plan}

---

## 8️⃣ 🧪 Basic Test Plan
- Unit tests for controllers  
- Integration tests for API routes  
- Validation tests for request bodies  
- Database migration tests  
- Basic load testing (optional)

---
"""


#
# from google import genai
# from backend.config.settings import GENAI_API_KEY
#
# client = genai.Client()
#
# def handle_project_task(message: str, intent: str = "plan"):
#     # For Day2, we call LLM to create a structured plan
#     prompt = f"""
# You are a senior software engineer. The user requests a project:
#
# {message}
#
# Produce a structured response containing:
# 1) Short summary
# 2) Suggested tech stack
# 3) Folder structure (code block)
# 4) Entities and ERD description (text)
# 5) API list (method, path, purpose)
# 6) Step-by-step implementation plan
# 7) Basic test plan
#
# Return as plain text with headings.
# """
#     res = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
#     return res.text
#



# """
# Project Builder Agent entry point.
# """
#
# from .folder_structure_generator import generate_folder_structure
# from .erd_generator import generate_erd_description
# from .api_list_generator import generate_api_list
# from .model_controller_generator import generate_models_and_controllers_plan
# from .project_planner import generate_step_by_step_plan
#
#
# def handle_project_query(message: str, session_id: str | None = None) -> str:
#     # TODO: Replace with multi-step agent planning using ADK.
#     parts = []
#
#     parts.append("📁 Folder Structure:\n" + generate_folder_structure(message))
#     parts.append("\n🧩 ER Diagram (text description):\n" + generate_erd_description(message))
#     parts.append("\n📡 API List:\n" + generate_api_list(message))
#     parts.append("\n🧱 Models & Controllers Plan:\n" + generate_models_and_controllers_plan(message))
#     parts.append("\n🪜 Step-by-Step Plan & Test Plan:\n" + generate_step_by_step_plan(message))
#
#     return "\n\n".join(parts)
