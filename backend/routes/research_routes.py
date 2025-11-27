from flask import Blueprint, request, jsonify
from backend.agents.research_agent.research_agent import handle_research

research_bp = Blueprint("research_bp", __name__)

@research_bp.post("/research")
def research():
    data = request.json or {}
    topic = data.get("topic", "")

    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    reply = handle_research(topic)

    return jsonify({
        "agent": "research",
        "reply": reply
    })
