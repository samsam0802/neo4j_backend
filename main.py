from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel # 이 줄이 없다면 추가


# ✅ 요청 바디 모델 정의
class GenerateRequest(BaseModel):
    count: int
    
app = FastAPI(title="강민석 반가워", version="1.0.0")

# ✅ [수정] 프론트엔드 주소 허용 (CORS)
origins = [
    "https://neo4j-frontend-iota.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}


@app.get("/")
def read_root():
    return {"message": "안녕 반가워"}