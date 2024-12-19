from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class Artigo(Base):
    __tablename__ = "artigo"

    id = Column(Integer(), primary_key=True)
    titulo = Column(String(255), nullable=False)
    conteudo = Column(Text, nullable=False)
    data_publicacao = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    data_atualizacao = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    tag = Column(String(50))
