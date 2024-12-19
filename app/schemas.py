from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class ArtigoBase(BaseModel):
    titulo: str
    conteudo: str


class ArtigoPublicacao(ArtigoBase):
    tags: Optional[List[str]] = []


class Artigo(ArtigoBase):
    id: int
    data_publicacao: datetime
    data_atualizacao: datetime
    tags: List[str]

    class Config:
        from_attributes = True
