from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ----------------- Database Configuration -----------------
# SQLite for demo; you can switch to PostgreSQL/MySQL by changing DATABASE_URL
DATABASE_URL = "sqlite:///./alzheimers.db"

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()

# ----------------- Dependency -----------------
# Use this in FastAPI routes to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
