from typing import List, Optional
from pydantic import BaseModel,EmailStr

class bookBase(BaseModel):
    book_id:int
    genre:str
    title:str
    author:str
    publisher:str

class books(bookBase):
    class Config():
        orm_mode = True

class users(BaseModel):
    name:str
    email:EmailStr
    password:str

class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[EmailStr] = None