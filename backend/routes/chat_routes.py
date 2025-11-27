# backend/routes/chat_routes.py


# backend/routes/chat_routes.py
from flask import Blueprint, request, jsonify
from backend.agents.root_router_agent import route_message
from backend.services.session_service import session_exists, create_new_session
from backend.utils.logger import log_event

chat_bp = Blueprint("chat_bp", __name__)


@chat_bp.post("/chat")
def chat():
    data = request.json or {}

    message = data.get("message", "").strip()
    forced_agent = data.get("agent", "auto")
    session_id = data.get("session_id")

    # ---- Log incoming message ----
    log_event("user_message", {
        "session_id": session_id,
        "forced_agent": forced_agent,
        "message": message
    })

    # ---- Validate message ----
    if not message:
        return jsonify({
            "reply": "Please type something to continue.",
            "agent": "system"
        }), 400

    # ---- Session check ----
    if not session_id or not session_exists(session_id):
        session_id = create_new_session()

    # ===================================================
    #     FORCED AGENT MODE (Sidebar override)
    # ===================================================
    if forced_agent != "auto":

        # ----- Coding Agent -----
        if forced_agent == "coding":
            from backend.agents.coding_agent.coding_agent import handle_coding_task
            reply = handle_coding_task(message, intent="explain")
            agent_used = "coding"

        # ----- Learning Agent -----
        elif forced_agent == "learning":
            from backend.agents.learning_agent.learning_agent import handle_learning_task
            reply = handle_learning_task(message, intent="teach", session_id=session_id)
            agent_used = "learning"

        # ----- Project Builder Agent -----
        elif forced_agent == "project":
            from backend.agents.project_builder_agent.project_agent import handle_project_task
            reply = handle_project_task(message, intent="plan")
            agent_used = "project"

        # ----- Code Review Agent -----
        elif forced_agent == "code_review":
            from backend.agents.code_review_agent.code_review_agent import handle_code_review
            reply = handle_code_review(message)
            agent_used = "code_review"

        # ----- Research Agent -----
        elif forced_agent == "research":
            from backend.agents.research_agent.research_agent import handle_research
            reply = handle_research(message)
            agent_used = "research"

        # ----- Document Reader Agent -----
        elif forced_agent == "document_reader":
            from backend.agents.document_reader_agent.document_agent import handle_document_task
            reply = handle_document_task(message)
            agent_used = "document_reader"

        else:
            reply = "Unknown agent selected."
            agent_used = "system"

    # ===================================================
    #               AUTO MODE → Root Router
    # ===================================================
    else:
        routed = route_message(message, session_id=session_id)
        reply = routed.get("reply")
        agent_used = routed.get("agent", "unknown")

    # ---- Log outgoing reply ----
    log_event("agent_reply", {
        "session_id": session_id,
        "agent": agent_used,
        "reply": reply
    })

    # ---- Final response ----
    return jsonify({
        "session_id": session_id,
        "agent": agent_used,
        "reply": reply
    })




# from flask import Blueprint, request, jsonify
# from backend.agents.root_router_agent import route_message
# from backend.services.session_service import session_exists, create_new_session
# from backend.utils.logger import log_event
#
# chat_bp = Blueprint("chat_bp", __name__)
#
#
# @chat_bp.post("/chat")
# def chat():
#     data = request.json or {}
#
#     message = data.get("message", "").strip()
#     forced_agent = data.get("agent", "auto")
#     session_id = data.get("session_id")
#
#     # ---- Logging incoming request ----
#     log_event("user_message", {
#         "session_id": session_id,
#         "forced_agent": forced_agent,
#         "message": message
#     })
#
#     # ---- Validate message ----
#     if not message:
#         return jsonify({
#             "error": "Message cannot be empty.",
#             "reply": "Please type something to continue.",
#             "agent": "system"
#         })
#
#     # ---- Ensure session exists ----
#     if not session_id or not session_exists(session_id):
#         session_id = create_new_session()
#
#     # ------------------------------
#     #  AGENT OVERRIDE MODE (Sidebar)
#     # ------------------------------
#     if forced_agent != "auto":
#         if forced_agent == "coding":
#             from backend.agents.coding_agent.coding_agent import handle_coding_task
#             reply = handle_coding_task(message, intent="explain")
#             agent_used = "coding"
#
#         elif forced_agent == "learning":
#             from backend.agents.learning_agent.learning_agent import handle_learning_task
#             reply = handle_learning_task(message, intent="teach", session_id=session_id)
#             agent_used = "learning"
#
#         elif forced_agent == "project":
#             from backend.agents.project_builder_agent.project_agent import handle_project_task
#             reply = handle_project_task(message, intent="plan")
#             agent_used = "project"
#
#
#
#         else:
#             reply = "Unknown agent selected."
#             agent_used = "system"
#
#     # ------------------------------
#     #  AUTO MODE → Root Router
#     # ------------------------------
#     else:
#         routed = route_message(message, session_id=session_id)
#         reply = routed.get("reply")
#         agent_used = routed.get("agent", "unknown")
#
#     # ---- Logging agent's reply ----
#     log_event("agent_reply", {
#         "session_id": session_id,
#         "agent": agent_used,
#         "reply": reply
#     })
#
#     return jsonify({
#         "session_id": session_id,
#         "agent": agent_used,
#         "reply": reply
#     })

# @chat_bp.post("/chat")
# def chat():
#     data = request.json or {}
#     message = data.get("message", "")
#     session_id = data.get("session_id")
#
#     log_event("user_message", {"session_id": session_id, "message": message})
#
#     if not session_id or not session_exists(session_id):
#         session_id = create_new_session()
#
#     routed = route_message(message, session_id=session_id)
#
#     log_event("agent_reply", {
#         "session_id": session_id,
#         "agent": routed.get("agent"),
#         "reply": routed.get("reply")
#     })
#
#     return jsonify({
#         "session_id": session_id,
#         "agent": routed.get("agent"),
#         "reply": routed.get("reply")
#     })
#

# @chat_bp.post("/chat")
# def chat():
#     data = request.json or {}
#     message = data.get("message", "")
#     session_id = data.get("session_id")
#
#     if not session_id or not session_exists(session_id):
#         session_id = create_new_session()
#
#     routed = route_message(message, session_id=session_id)
#     # routed is a dict with agent and reply
#     return jsonify({
#         "session_id": session_id,
#         "agent": routed.get("agent"),
#         "reply": routed.get("reply")
#     })




# from flask import Blueprint, request, jsonify
# from backend.agents.root_router_agent import route_message
# from backend.services.session_service import session_exists, create_new_session
#
# chat_bp = Blueprint("chat_bp", __name__)
#
# @chat_bp.post("/chat")
# def chat():
#     data = request.json
#     message = data.get("message", "")
#     session_id = data.get("session_id")
#
#     # Create new session if not exists
#     if not session_id or not session_exists(session_id):
#         session_id = create_new_session()
#
#     reply = route_message(message)
#
#     return jsonify({
#         "session_id": session_id,
#         "reply": reply,
#         "agent": "coding_agent"
#     })



# from flask import Blueprint, request, jsonify
# from agents.root_router_agent import route_message
#
# chat_bp = Blueprint("chat_bp", __name__)
#
# @chat_bp.post("/chat")
# def chat():
#     data = request.get_json() or {}
#     user_message = data.get("message", "")
#     session_id = data.get("session_id")
#
#     response = route_message(user_message, session_id)
#     return jsonify({"response": response})
