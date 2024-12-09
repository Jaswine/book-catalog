from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


engine = create_engine(f'postgresql://{getenv("DATABASE_USERNAME", "book_catalog")}:{getenv("DATABASE_PASSWORD", "book_catalog")}@{getenv("DATABASE_HOST", "localhost")}/{getenv("DATABASE_NAME", "book_catalog")}',
                       pool_pre_ping=True, echo=True)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Зависимость для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()