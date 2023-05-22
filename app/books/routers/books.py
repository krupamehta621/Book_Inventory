from fastapi import APIRouter
from typing import List
from fastapi import FastAPI,Response,status,Depends,Query,HTTPException
from sqlalchemy.orm import Session
from ..repository import books
from ... import schema,models,database,oauth2
from fastapi_pagination import Page,add_pagination,paginate

router=APIRouter(
    prefix='/books',
    tags=["Books"]
)

@router.get("")
def read_all( db:Session = Depends(database.get_db),sort_by:str=Query(default='book_id',description="field")):
    return  books.read_all(db,sort_by)

@router.post("", status_code=status.HTTP_201_CREATED)
def create(request:schema.books , db:Session = Depends(database.get_db)):
    return books.create(request,db)

@router.get("/{book_id}",status_code=200, response_model=schema.books)
def read(book_id:int,response:Response,db:Session = Depends(database.get_db)):
    return books.read(book_id,db)

@router.put('/{book_id}',status_code=status.HTTP_202_ACCEPTED)
def update_record(book_id:int,request:schema.books,db:Session = Depends(database.get_db)):
    return books.update_record(book_id,request,db)

@router.delete('/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(book_id:int,db:Session = Depends(database.get_db)):
    return books.delete(book_id,db)