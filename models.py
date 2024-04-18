# SQLAlchemy를 이용하여 데이터베이스 모델을 정의합니다.
# Sentence라는 클래스를 정의하여, 법적 사례에 대한 정보를 데이터베이스에 저장할 수 있는 구조를 만들고 있습니다. 

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()  # SQLAlchemy 모델의 기본 클래스를 생성합니다.

class Sentence(Base):  # 데이터베이스 테이블과 매핑될 클래스를 정의합니다.
    __tablename__ = 'sentence'  # 데이터베이스 내에서 사용될 테이블의 이름입니다.
    
    id = Column(Integer, primary_key=True, index=True)  # 고유한 식별자 역할을 하는 기본 키입니다.
    title = Column(String)  # 사례의 제목을 저장하는 필드입니다.
    case_number = Column(String)  # 사례 번호를 저장하는 필드입니다.
    content = Column(String)  # 사례의 내용을 저장하는 필드입니다.
    similar_case = Column(String)  # 유사한 사례를 나타내는 필드입니다.
    cur_idx = Column(Integer)  # 현재 인덱스를 저장하는 필드입니다.
    link = Column(String)  # 사례와 관련된 링크를 저장하는 필드입니다.
