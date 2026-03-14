from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = [
    "http://localhost",
    "https://xpert-drwq.onrender.com/", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "준상의 3D 게임 API 서버 작동 중!"}

# 월드랭킹 예시 API
@app.get("/ranking")
def get_ranking():
    # 나중에 여기에 DB 연동 (PostgreSQL)
    return [{"name": "User1", "score": 100}, {"name": "User2", "score": 80}]
