from fastapi import FastAPI,Response,status,Depends,HTTPException
from . import schema,models
from .database import engine
from app.books.routers import books,users,authentication
from fastapi_pagination import Page,add_pagination

models.base.metadata.create_all(engine)

app=FastAPI()
add_pagination(app)
app.include_router(authentication.router)
app.include_router(books.router)
app.include_router(users.router)
