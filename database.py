# Python에서 환경 변수를 로드하고, MySQL 데이터베이스에 연결하여 데이터를 가져오는 과정입니다.
# SQLAlchemy와 PyMySQL을 사용하여 데이터베이스 엔진 및 세션을 생성하고,
# 데이터를 조회하는 기능을 구현합니다.

import os  # 운영체제와 상호작용하기 위한 모듈
import pymysql  # MySQL 데이터베이스를 사용하기 위한 모듈
import pandas as pd  # 데이터 처리를 위한 pandas 라이브러리
from dotenv import load_dotenv  # .env 파일로부터 환경 변수를 로드하기 위한 모듈
from sqlalchemy import create_engine  # SQLAlchemy를 통해 데이터베이스 엔진을 생성하기 위한 함수
from sqlalchemy.orm import sessionmaker  # SQLAlchemy 세션을 생성하기 위한 함수

load_dotenv()  # .env 파일로부터 환경 변수 로드

# 환경 변수로부터 데이터베이스 설정 정보 가져오기
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# 데이터베이스 접속 URL 구성
DB_URL = f'mysql+pymysql://{user}:{password}@{host}:3306/{db_name}'

# SQLAlchemy 엔진 및 세션 생성
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def fetch_data():
    # pymysql을 사용하여 데이터베이스 연결
    connection = pymysql.connect(host=host, user=user, password=password, database=db_name)
    try:
        # 데이터 조회 쿼리 실행
        query = "SELECT title, vector FROM sentence"
        datas = pd.read_sql_query(query, connection)  # 특정 컬럼 조회 결과

        alldataquery = "SELECT * FROM sentence"
        data_list = pd.read_sql_query(alldataquery, connection)  # 전체 컬럼 조회 결과
    finally:
        connection.close()  # 연결 종료

    return datas, data_list  # 조회 결과 반환

def get_db():
    # SQLAlchemy 세션 생성 및 제공
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # 세션 종료
