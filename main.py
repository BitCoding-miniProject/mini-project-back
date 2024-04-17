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

model = SentenceTransformer("jhgan/ko-sroberta-multitask")



@app.post("/comparefile/", summary="검색값 임베딩 후 결과 출력", description="사용자가 검색할 문장을 입력하고, 가장 유사한 title을 출력합니다. 사용자 입력값을 필수로 제공해야 합니다.")
async def create_upload_file(contents: str = Form(...)):
    datas, _ = fetch_data()

    sentences = datas['title'].tolist()
    embeddings = np.stack(datas['vector'].apply(lambda x: np.fromstring(x.strip("[]"), sep=' ')))
    embeddings = torch.tensor(embeddings).float()


    queries = [contents]
    top_k = 5
    query_embedding = model.encode(queries, convert_to_tensor=True).float()


    response_data = []  

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
    item = db.query(Sentence).filter(Sentence.id == item_id).first()
    if item is not None:
        return item
    else:
        raise HTTPException(status_code=404, detail="Item not found")



@app.post("/alllist/", summary="모든 판례 조회", description="임베딩 데이터를 제회한 모든 판례를 조회합니다.")
async def allfiles():
    _, data_list = fetch_data()
    
    records = data_list.to_dict(orient='records')
    
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
