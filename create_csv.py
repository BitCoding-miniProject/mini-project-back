# SQLAlchemy ORM을 사용하여 데이터베이스에서 모든 데이터를 조회한 후, 이를 텍스트 파일로 저장합니다.

from sqlalchemy.orm import Session  # SQLAlchemy ORM에서 Session을 임포트합니다.
from database import SessionLocal  # 데이터베이스 설정에서 정의한 SessionLocal을 임포트합니다.
import parse  # parse 모듈을 임포트합니다. (이 코드에서는 사용되지 않는 것으로 보입니다.)
import models  # 데이터베이스 모델을 정의한 모듈을 임포트합니다.

db = SessionLocal()  # 데이터베이스 세션 인스턴스를 생성합니다.

def get_all_data():
    # 데이터베이스에서 모든 'Case' 데이터를 조회하는 함수입니다.
    return db.query(models.Case).all()

with open('data.txt', 'w') as data_csv:  # 'data.txt' 파일을 쓰기 모드로 엽니다.
    for e in get_all_data():  # 데이터베이스에서 조회한 모든 데이터에 대해 반복 처리합니다.
        # 각 필드를 문자열로 변환하고 쉼표로 구분하여 리스트로 만듭니다.
        fields = [str(e.id), e.case_number, e.title, e.content, str(e.vector), str(e.similar_case), str(e.cur_idx), e.link]
        data_csv.write(",".join(fields))  # 리스트를 문자열로 변환하여 파일에 씁니다.

