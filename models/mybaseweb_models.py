# base_end/models/mybaseweb_models.py
from sqlalchemy import Column, Integer, String
from database.mybaseweb_db import Base

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(String(255), nullable=False)
