# FastAPI를 사용하여 생성된 웹 애플리케이션의 메인 기능입니다.
# 코드는 사용자로부터 입력받은 문장과 데이터베이스 내 문장들 간의 유사도를 계산하고,
# 가장 유사한 문장들을 찾아 반환하는 기능을 구현합니다.
# 특정 판례를 조회하거나 모든 판례를 조회하는 기능도 포함하고 있습니다. 

from http.client import HTTPException
from fastapi import Depends, FastAPI, Form
import numpy as np
from requests import Session
import torch
from database import fetch_data
from sentence_transformers import SentenceTransformer, util
from fastapi.responses import JSONResponse
import pandas as pd
from models import Sentence
from database import get_db
from schemas import SentenceSchema

app = FastAPI()

# 문장 임베딩 모델 로드
model = SentenceTransformer("jhgan/ko-sroberta-multitask")




@app.post("/comparefile/", summary="검색값 임베딩 후 결과 출력", description="사용자가 검색할 문장을 입력하고, 가장 유사한 title을 출력합니다. 사용자 입력값을 필수로 제공해야 합니다.")
async def create_upload_file(contents: str = Form(...)):
    datas, _ = fetch_data()  # 데이터베이스에서 데이터 가져오기

    # 제목과 벡터를 리스트 및 텐서로 변환
    sentences = datas['title'].tolist()
    embeddings = np.stack(datas['vector'].apply(lambda x: np.fromstring(x.strip("[]"), sep=' ')))
    embeddings = torch.tensor(embeddings).float()

    # 사용자 쿼리 임베딩
    queries = [contents]
    top_k = 5
    query_embedding = model.encode(queries, convert_to_tensor=True).float()

    response_data = []  # 응답 데이터 준비

    # 유사도 계산 및 상위 결과 선택
    for query in queries:
        cos_scores = util.pytorch_cos_sim(query_embedding, embeddings)[0]
        cos_scores = cos_scores.cpu()

        top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]
        
        query_response = {"query": query, "matches": []}
        for idx in top_results[0:top_k]:
            match_data = {
                "title": sentences[idx],
                "score": float(cos_scores[idx]) 
            }
            query_response["matches"].append(match_data)

        response_data.append(query_response)

    return JSONResponse(content={"responses": response_data})



@app.get("/item/{item_id}", response_model=SentenceSchema, summary="판례 조회", description="등록번호로 판례를 조회하고 데이터를 출력합니다.")
async def read_item(item_id: int, db: Session = Depends(get_db)):
    # 특정 판례 조회
    item = db.query(Sentence).filter(Sentence.id == item_id).first()
    if item is not None:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")




@app.post("/alllist/", summary="모든 판례 조회", description="임베딩 데이터를 제회한 모든 판례를 조회합니다.")
async def allfiles():
    _, data_list = fetch_data()  # 데이터베이스에서 모든 데이터 가져오기
    
    records = data_list.to_dict(orient='records')  # 데이터프레임을 딕셔너리 리스트로 변환
    
    # 필요한 정보만 선택하여 리스트 생성
    combined_list = [{
        "id": item["id"],
        "title": item["title"],
        "case_number": item["case_number"],
        "content": item["content"],
        "similar_case": item["similar_case"],
        "cur_idx": item["cur_idx"],
        "link": item["link"],
    } for item in records]

    return JSONResponse(content={"responses": combined_list})
