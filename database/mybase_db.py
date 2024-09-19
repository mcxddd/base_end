from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import MYBASEWEB_DATABASE_URL

# 使用 Oracle 连接
engine = create_engine(MYBASEWEB_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_mybaseweb_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
