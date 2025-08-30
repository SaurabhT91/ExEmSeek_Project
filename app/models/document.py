from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field

class Document(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    publication_date: date
    publisher: Optional[str] = None
    description: Optional[str] = None
    document_type: Optional[str] = None   # "research_paper", "article", "thesis"
    thumbnail_url: Optional[str] = None   # link/path to thumbnail image
    language: Optional[str] = None
    file_path: Optional[str] = None       # path or URL to original PDF file
