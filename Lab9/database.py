# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Подключение к PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/LabDB"
# замени логин/пароль/хост/порт под себя

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


# dependency для FastAPI и для скриптов
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
