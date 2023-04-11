from pydantic import BaseModel
from datetime import date
from typing import List

class Genre(BaseModel):
    name: str
class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    # = None Если атрибут может быть необязателен
    genres: List[Genre]
    pages: int