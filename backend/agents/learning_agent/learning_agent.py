# backend/agents/learning_agent/learning_agent.py
from .topic_explainer import explain_topic
from .notes_generator import generate_notes
from .quiz_generator import generate_quiz
from .mindmap_generator import generate_mindmap
from backend.services.db_service import db_session
from backend.database.models.learning_progress_model import LearningProgress

def handle_learning_task(message: str, intent: str = "teach", session_id: str = None):
    """
    intent: teach | notes | quiz | mindmap
    """
    if intent == "teach":
        return explain_topic(message)
    if intent == "notes":
        notes = generate_notes(message)
        # optionally store notes for session
        if session_id:
            with db_session() as db:
                lp = LearningProgress(session_id=session_id, topic=extract_topic(message), notes=notes)
                db.add(lp)
        return notes
    if intent == "quiz":
        quiz_text = generate_quiz(message)
        return quiz_text
    if intent == "mindmap":
        return generate_mindmap(message)
    # default
    return explain_topic(message)

def extract_topic(message: str):
    # naive extraction: first few words; can improve
    return message.strip().split("\n")[0][:150]



# """
# Topic Learning Agent entry point.
# """
#
# from .topic_explainer import explain_topic
# from .notes_generator import generate_notes
# from .quiz_generator import generate_quiz
# from .mindmap_generator import generate_mindmap
#
#
# def handle_learning_query(message: str, session_id: str | None = None) -> str:
#     msg_lower = message.lower()
#
#     if "note" in msg_lower or "summary" in msg_lower:
#         return generate_notes(message)
#     if "quiz" in msg_lower or "mcq" in msg_lower:
#         return generate_quiz(message)
#     if "mind map" in msg_lower or "mindmap" in msg_lower:
#         return generate_mindmap(message)
#
#     # Default behavior: explain topic
#     return explain_topic(message)
