from sqlalchemy.orm import Session
from ... import schema,models
from fastapi import HTTPException, Query, status
from fastapi_pagination import Page,add_pagination,paginate

def read_all(db: Session,sort_by:str=Query(default='book_id',description="field")):#filtering: str=Query(description="field")|None=None)
   
    booksOut=db.query(models.books).all()
    if sort_by not in ['book_id','genre','title','author','publisher']:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        if sort_by=='genre':
            sorted_books=sorted(booksOut,key=lambda x:x.genre)
        elif sort_by=='title':
            sorted_books=sorted(booksOut,key=lambda x:x.title)
        elif sort_by=='publisher':
            sorted_books=sorted(booksOut,key=lambda x:x.publisher)
        elif sort_by=='author':
            sorted_books=sorted(booksOut,key=lambda x:x.author)
        else:
            sorted_books=sorted(booksOut,key=lambda x:x in x.book_id)
        return (sorted_books)


def create(request: schema.books, db: Session):
    new_book=models.books(book_id=request.book_id ,genre=request.genre ,title=request.title ,author=request.author ,publisher=request.publisher)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def delete(book_id: int, db: Session):
    books=db.query(models.books).filter(models.books.book_id==book_id)
    if not books.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f'Book with id {book_id} not found')

    books.delete(synchronize_session=False)
    db.commit()
    return {"Deleted"}

    
    
def update_record(book_id: int, request: schema.books, db: Session):
    books=db.query(models.books).filter(models.books.book_id==book_id)
    
    if not books.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f'Book with id {book_id} not found')
    
    books.update({'genre':request.genre ,'title':request.title ,'author':request.author ,'publisher':request.publisher})
    db.commit()
    return "Updated the record"
    

def read(book_id: int, db: Session):
    books=db.query(models.books).filter(models.books.book_id==book_id).first()
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The given book id {book_id} does not exist")
    
    return books