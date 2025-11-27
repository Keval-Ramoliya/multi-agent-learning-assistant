from flask import Blueprint, jsonify
from backend.services.session_service import create_new_session

session_bp = Blueprint("session_bp", __name__)

@session_bp.get("/session")
def create_session():
    new_id = create_new_session()
    return jsonify({"session_id": new_id})



# from flask import Blueprint, request, jsonify
# from services.session_service import create_new_session, get_or_create_session
#
# session_bp = Blueprint("session_bp", __name__)
#
# @session_bp.post("/session")
# def create_session():
#     data = request.get_json() or {}
#     user_id = data.get("user_id")
#     session_id = create_new_session(user_id)
#     return jsonify({"session_id": session_id})
#
# @session_bp.get("/session/<user_id>")
# def get_session(user_id):
#     session_data = get_or_create_session(user_id)
#     return jsonify(session_data)
