from fastapi import APIRouter,Response,status,Depends,HTTPException
from sqlalchemy.orm import Session
from ... import schema,models,database
from ..repository import users

router=APIRouter(
    prefix='/user',
    tags=["User"]
)


@router.post('/')
def create_user(request :schema.users,db:Session = Depends(database.get_db)):
    return users.create_user(request,db)

@router.get('/{id}')
def get_user(id:int,db:Session = Depends(database.get_db)):
    return users.get_user(id,db)