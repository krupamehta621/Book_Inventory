from .database import base
from  sqlalchemy import Column,Integer,String

class books(base):
    __tablename__="books"
    
    book_id= Column(Integer,primary_key=True,index=True)
    genre=Column(String)
    title=Column(String)
    author=Column(String)
    publisher=Column(String)

class users(base):
    __tablename__="users"

    id= Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)