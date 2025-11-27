# backend/agents/root_router_agent.py
import json
from typing import Dict, Any
from backend.utils.json_validator import safe_parse_router_json
from backend.config.settings import GENAI_API_KEY

# We'll lazily import handlers to avoid circular imports
def route_message(message: str, session_id: str = None) -> Dict[str, Any]:
    """
    Tries rule-based first (fast). If undecided, fallback to LLM router.
    Returns a dict: { "agent": "coding"|"learning"|"project", "intent": "...", "arguments": {...}, "reply": "..." }
    """

    m = message.lower()

    # RULE-BASED quick routing for common coding keywords (fast)
    if any(k in m for k in ["explain", "what does this code do", "line by line"]):
        from backend.agents.coding_agent.coding_agent import handle_coding_task
        return {"agent": "coding", "reply": handle_coding_task(message, intent="explain")}

    if any(k in m for k in ["error", "debug", "fix", "traceback"]):
        from backend.agents.coding_agent.coding_agent import handle_coding_task
        return {"agent": "coding", "reply": handle_coding_task(message, intent="debug")}

    if any(k in m for k in ["teach", "explain concept", "what is", "bfs", "binary", "sql", "machine learning", "ml"]):
        from backend.agents.learning_agent.learning_agent import handle_learning_task
        # default intent teach
        return {"agent": "learning", "reply": handle_learning_task(message, intent="teach", session_id=session_id)}

    if any(k in m for k in ["project", "api list", "folder structure", "erd", "database schema"]):
        from backend.agents.project_builder_agent.project_agent import handle_project_task
        return {"agent": "project", "reply": handle_project_task(message, intent="plan")}

    # FALLBACK: Use LLM router to decide
    try:
        # Use google-genai
        from google import genai
        client = genai.Client()
        prompt = f"""
You are a router that decides which agent should handle the user's message.
Return only valid JSON with keys: target_agent, intent, arguments.
Allowed agents: coding, learning, project.

User message:
\"\"\"{message}\"\"\"

Example valid response:
{{"target_agent":"coding", "intent":"code_debug", "arguments":{{"language":"python"}}}}
"""
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        text = response.text.strip()
        parsed = safe_parse_router_json(text)
        if parsed:
            # call the chosen agent
            agent = parsed.get("target_agent")
            intent = parsed.get("intent")
            args = parsed.get("arguments", {})
            if agent == "coding":
                from backend.agents.coding_agent.coding_agent import handle_coding_task
                return {"agent": "coding", "reply": handle_coding_task(message, intent=intent)}
            if agent == "learning":
                from backend.agents.learning_agent.learning_agent import handle_learning_task
                return {"agent": "learning", "reply": handle_learning_task(message, intent=intent, session_id=session_id)}
            if agent == "project":
                from backend.agents.project_builder_agent.project_agent import handle_project_task
                return {"agent": "project", "reply": handle_project_task(message, intent=intent)}
    except Exception as e:
        # fallback safe message
        return {"agent": "unknown", "reply": "Sorry — I couldn't route your message. Try 'Explain code' or 'Teach me BFS'."}

    return {"agent": "unknown", "reply": "Couldn't determine agent."}




# # root_router_agent.py
# import json
# from backend.backend.agents.coding_agent.coding_agent import handle_coding_task
#
# def route_message(message: str):
#     """
#     Simple Rule-Based Router for Day-1.
#     Later we will replace with ADK LLM Router.
#     """
#
#     msg = message.lower()
#
#     if any(x in msg for x in ["explain", "what does this code do", "meaning"]):
#         return handle_coding_task(message, intent="explain")
#
#     if any(x in msg for x in ["error", "bug", "debug", "fix"]):
#         return handle_coding_task(message, intent="debug")
#
#     if any(x in msg for x in ["optimize", "better", "faster", "improve"]):
#         return handle_coding_task(message, intent="optimize")
#
#     if any(x in msg for x in ["test case", "testcase", "sample input"]):
#         return handle_coding_task(message, intent="testcase")
#
#     # Default fallback → explain code
#     return handle_coding_task(message, intent="explain")


# """
# Root router agent: decides which sub-agent to call
# based on user intent (coding, learning, project building).
# """
#
# def route_message(message: str, session_id: str | None = None) -> str:
#     # Very simple placeholder routing for now
#     msg_lower = message.lower()
#
#     if any(k in msg_lower for k in ["bug", "error", "code", "optimize", "debug"]):
#         from agents.coding_agent.coding_agent import handle_coding_query
#         return handle_coding_query(message, session_id)
#
#     if any(k in msg_lower for k in ["learn", "explain", "topic", "dsa", "sql", "ml"]):
#         from agents.learning_agent.learning_agent import handle_learning_query
#         return handle_learning_query(message, session_id)
#
#     if any(k in msg_lower for k in ["project", "folder", "api", "model", "controller", "erd"]):
#         from agents.project_builder_agent.project_agent import handle_project_query
#         return handle_project_query(message, session_id)
#
#     # Default: treat as learning request
#     from agents.learning_agent.learning_agent import handle_learning_query
#     return handle_learning_query(message, session_id)
