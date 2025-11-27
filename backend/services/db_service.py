# backend/services/db_service.py
from contextlib import contextmanager
from backend.database.db import SessionLocal

@contextmanager
def db_session():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()



# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from config.settings import SQLALCHEMY_DATABASE_URL
#
# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, future=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
