from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Sentence(Base):
    __tablename__ = 'sentence'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    case_number = Column(String)
    content = Column(String)
    similar_case = Column(String)
    cur_idx = Column(Integer)
    link = Column(String)
