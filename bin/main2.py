


# class Texts(BaseModel):
#     texts: List[str]

# @app.post("/transform/")
# async def transform(texts: str = Form(...)):
#     try:
#         # 입력된 텍스트에 대해 임베딩을 계산
#         embeddings = model.encode(texts, show_progress_bar=False)
#         # 임베딩 결과를 반환
#         return embeddings.tolist()
#     except Exception as e:
#         # 에러 처리
#         raise HTTPException(status_code=500, detail=str(e))

@app.post("/transform/")
async def transform_text(item: str = Form(...)):
    # 맨 앞과 뒤에 추가할 [[]]와 함께 ','를 삭제합니다.
    transformed_text = f'[[{item.replace(",", "")}]]'
    return transformed_text
