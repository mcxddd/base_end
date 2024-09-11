# base_end/services/mybaseweb_service.py
from re import S
from sqlalchemy.orm import Session
from models.mybaseweb_models import Post

def create_post(db: Session, title: str, content: str):
    new_post = Post(title=title, content=content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db: Session):
    return db.query(Post).all()
