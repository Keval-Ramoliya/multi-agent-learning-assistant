from flask import Blueprint, request, jsonify
import os

from backend.agents.document_reader_agent.pdf_reader import extract_text_from_pdf
from backend.agents.document_reader_agent.document_agent import handle_document_task

document_bp = Blueprint("document_bp", __name__)

UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# STEP 1 — Upload PDF + Extract Text
@document_bp.post("/upload-pdf")
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "File name is empty"}), 400

    upload_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(upload_path)

    text = extract_text_from_pdf(upload_path)

    return jsonify({"text": text})


# STEP 2 — Document Agent Analysis
@document_bp.post("/document-text")
def document_text():
    data = request.json or {}
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    reply = handle_document_task(text)

    return jsonify({
        "agent": "document_reader",
        "reply": reply
    })
