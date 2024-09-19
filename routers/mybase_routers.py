# base_end/routers/mybaseweb.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.mybase_models import Post
from database.mybase_db import get_mybaseweb_db
from services.mybase_service import create_post, get_all_posts

router = APIRouter()

@router.get("/posts/")
def read_posts(db: Session = Depends(get_mybaseweb_db)):
    return get_all_posts(db)

@router.post("/posts/")
def add_post(title: str, content: str, db: Session = Depends(get_mybaseweb_db)):
    return create_post(db, title, content)
