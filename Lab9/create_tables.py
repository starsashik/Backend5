# create_tables.py
from database import engine, Base
import models  # важно: импортируем, чтобы Base "видел" модели

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы.")
