# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from backend.config.settings import DB_URI
#
# engine = create_engine(DB_URI, echo=False, future=True)
# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
# Base = declarative_base()
#
# def init_db():
#     import backend.database.models  # noqa: F401 - imports models so they register with Base
#     Base.metadata.create_all(bind=engine)
#
#



import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read DB fields from environment variables
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "multi_agent_db")

# Construct full URI
DB_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"

# Create engine
engine = create_engine(DB_URI, echo=False, future=True)

# Session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base model
Base = declarative_base()

def init_db():
    # Import models so SQLAlchemy registers them
    import backend.database.models   # noqa: F401
    Base.metadata.create_all(bind=engine)
