from flask import Blueprint, request, jsonify
from backend.agents.code_review_agent.code_review_agent import handle_code_review

code_review_bp = Blueprint("code_review_bp", __name__)

@code_review_bp.post("/code-review")
def code_review():
    data = request.json or {}
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    reply = handle_code_review(code)

    return jsonify({
        "agent": "code_review",
        "reply": reply
    })
