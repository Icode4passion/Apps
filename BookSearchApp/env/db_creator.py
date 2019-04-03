from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///mybooks.db', echo=True)
Base = declarative_base()
 
class BooksDB(Base):
    """"""
    __tablename__ = "booksbd"
    id = Column(Integer,primary_key = True)
    book_title = Column(String)
    book_type = Column(String)
    authors = Column(String)
    UID = Column(Integer)
    publisher = Column(String)
    publish_date = Column(Integer)
    edition = Column(String)
    binding = Column(String)
# create tables
Base.metadata.create_all(engine)