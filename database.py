import os
import pymysql
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# DB_URL 구성을 위한 수정된 코드
DB_URL = f'mysql+pymysql://{user}:{password}@{host}:3306/{db_name}'

# SQLAlchemy 엔진 및 세션 생성
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def fetch_data():
    connection = pymysql.connect(host=host, user=user, password=password, database=db_name)
    try:
        query = "SELECT title, vector FROM sentence"
        datas = pd.read_sql_query(query, connection)

        alldataquery = "SELECT * FROM sentence"
        data_list = pd.read_sql_query(alldataquery, connection)
    finally:
        connection.close()

    return datas, data_list

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()







