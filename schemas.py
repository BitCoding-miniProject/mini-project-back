from pydantic import BaseModel

class SentenceSchema(BaseModel):
    id: int
    title: str
    case_number: str
    content: str
    similar_case: str
    cur_idx: int
    link: str

    class Config:
        orm_mode = True
