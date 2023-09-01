from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def root():
    return{"message: 인덱스 주소입니다"}


@app.get("/all") 
async def all_movies():
    result = random_items()
    return{"result": result}

@app.get("/genres/{genre}")
async def gerne_movies(genre: str):
    result = random_genres_items(genre)
    return {"result": result}
    
@app.get("/user_based")
async def user_based(params: Optional[List[str]] = Query(None)):
    return {"message":"user_based"}