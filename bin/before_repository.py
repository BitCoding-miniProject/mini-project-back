

# import pandas as pd
# import xml.etree.ElementTree as ET
# from urllib.request import urlopen
# from tqdm import trange
# import ssl
# from bs4 import BeautifulSoup as bs

# import model
# from models import Case
# import parse

# # SSL 인증서 검증을 비활성화
# ssl._create_default_https_context = ssl._create_unverified_context

# # DB에 저장할 더미 데이터 생성
# case_list = parse.get_case_list()

# # 법률 정보를 가져올 URL 설정
# # url = 'https://www.law.go.kr/DRF/lawSearch.do?OC=test&target=prec&type=XML&query=%EB%8B%B4%EB%B3%B4%EA%B6%8C'

# # 웹에서 XML 데이터를 가져옴
# # response = urlopen(url).read()

# # XML 데이터 파싱
# # xml_data = ET.fromstring(response)

# # 전체 데이터 개수 확인
# # totalCnt = int(xml_data.find('totalCnt').text)

# # 페이지당 데이터를 가져와서 처리
# # for i in trange(int(totalCnt / 20)):

#     # 데이터에서 필요한 정보 추출
#     # for info in prec_info:

#         # 추출한 정보를 바탕으로 Case 객체 생성 및 리스트에 추가
#         # case_list.append(
#         #     Case(title=case,
#         #         case_number=caseNum,
#         #         content=sentence,
#         #         vector=model.getSimilarity(sentence),
#         #         link=judicPrecLink)
#         #         )

# from sqlalchemy.orm import Session
# from database import SessionLocal
# import parse

# # 데이터베이스 세션 생성
# db = SessionLocal()

# def add_case(case: Case, db: Session):
#     # 데이터베이스에 케이스 추가
#     db.add(case)

# # 더미 데이터를 데이터베이스에 반복적으로 추가
# for e in case_list:
#     add_case(e, db)
# db.commit()

# def fetch_data(db: Session):
#     # 데이터베이스에서 모든 케이스 조회
#     return db.query(Case).all()

# # 데이터베이스에서 특정 ID를 가진 케이스 조회 및 출력
# # find = db.query(case.Case).filter(case.Case.id == 10).first()
# # print('find_id =', find.id)
# # print('find_vector =', find.similar_case['vector'])
