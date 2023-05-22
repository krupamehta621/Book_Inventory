from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine=create_engine( 'sqlite:///./book.db',connect_args={"check_same_thread": False})

SessionLocal=sessionmaker(bind=engine, autocommit=False, autoflush=False,)

base=declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()