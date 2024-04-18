# Pydantic 라이브러리를 사용하여 SentenceSchema라는 데이터 검증 및 설정 모델을 정의합니다. 
# 데이터베이스 모델과 유사한 구조를 가지며,
# 데이터를 JSON과 같은 다른 데이터 형식으로 쉽게 변환할 수 있게 해줍니다. 


from pydantic import BaseModel

class SentenceSchema(BaseModel):
    id: int
    title: str
    case_number: str
    content: str
    similar_case: str
    cur_idx: int
    link: str

# ORM 모델로부터 데이터를 읽는 데 사용될 수 있도록 허용합니다. 
    class Config:
        orm_mode = True
