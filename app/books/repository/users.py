from fastapi import APIRouter,Response,status,Depends,HTTPException
from sqlalchemy.orm import Session
from ... import schema,models,database
from ..hashing import Hash



def create_user(request :schema.users,db:Session):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int,db:Session):
    users=db.query(models.users).filter(models.users.id==id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The given user id {id} does not exist")
    
    return users