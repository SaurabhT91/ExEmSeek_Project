from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field

class Document(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    publication_date: date
    publisher: Optional[str]
    description: Optional[str]
