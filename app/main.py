#~/movie_service/app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]

class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]

@app.get('/', response_model=List[Movie])
async def index():
    return fake_movie_db

@app.post('/', status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}

