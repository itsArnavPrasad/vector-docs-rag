from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///pdf_data.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class PDFChunk(Base):
    __tablename__ = "pdf_chunks"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    chunk_text = Column(Text)
    chunk_number = Column(Integer)
    page_start = Column(Integer)
    page_end = Column(Integer)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized.")