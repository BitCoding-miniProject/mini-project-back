import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

from models import Sentence
from models import Sentence
import parse
from sqlalchemy.orm import Session
from database import SessionLocal
import parse

def add_case(case: Sentence, db: Session):
    db.add(case)


def fetch_data(db: Session):
    return db.query(Sentence).all()

ssl._create_default_https_context = ssl._create_unverified_context

db = SessionLocal()
user_id = 'wonje.j1996'
start_page = 1
show = 50

# DB에 데이터 추가
# for cur_page in range(start_page, 9):
#     url = f'https://www.law.go.kr/DRF/lawSearch.do?OC={user_id}&target=prec&type=XML&display={show}&page={cur_page}'
#     response = urlopen(url).read()
#     xml_data = ET.fromstring(response)
#     lst = parse.get_case_list(xml_data)
#     # 데이터 반복해서 DB에추가
#     for e in lst:
#         add_case(e, db)
#     db.commit()

