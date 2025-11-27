# backend/services/session_service.py
import uuid
from backend.services.db_service import db_session
from backend.database.models.session_model import Session as SessionModel
from datetime import datetime

def create_new_session(user_id=None):
    sid = str(uuid.uuid4())
    with db_session() as db:
        s = SessionModel(session_id=sid, user_id=user_id)
        db.add(s)
    return sid

def session_exists(session_id: str) -> bool:
    with db_session() as db:
        found = db.query(SessionModel).filter(SessionModel.session_id == session_id).first()
        return found is not None




# import uuid
# from datetime import datetime
#
# # TEMP in-memory session store (Day-1 only)
# SESSIONS = {}
#
# def create_new_session():
#     session_id = str(uuid.uuid4())
#     SESSIONS[session_id] = {"created_at": datetime.now()}
#     return session_id
#
# def session_exists(session_id):
#     return session_id in SESSIONS

#  --------------------------------------------------------------------

# import uuid
# from services.db_service import SessionLocal
# from database.models.session_model import Session
#
# def create_new_session(user_id: str | None = None) -> str:
#     db = SessionLocal()
#     new_id = str(uuid.uuid4())
#     session = Session(user_id=user_id, session_id=new_id)
#     db.add(session)
#     db.commit()
#     db.close()
#     return new_id
#
# def get_or_create_session(user_id: str | None = None) -> dict:
#     db = SessionLocal()
#     if user_id:
#         existing = db.query(Session).filter(Session.user_id == user_id).first()
#         if existing:
#             db.close()
#             return {"session_id": existing.session_id}
#     new_id = create_new_session(user_id)
#     return {"session_id": new_id}
