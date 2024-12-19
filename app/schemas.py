from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class ArtigoBase(BaseModel):
    titulo: str
    conteudo: str


class ArtigoPublicacao(ArtigoBase):
    tag: Optional[str] = None


class Artigo(ArtigoBase):
    id: int
    data_publicacao: datetime
    data_atualizacao: datetime
    tag: Optional[str] = None

    class Config:
        from_attributes = True
