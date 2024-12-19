from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
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

    tags = relationship("Tag", secondary="artigo_tag", back_populates="artigos")


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer(), primary_key=True)
    descricao = Column(String(50), unique=True, nullable=False)

    artigos = relationship("Artigo", secondary="artigo_tag", back_populates="tags")


class ArtigoTag(Base):
    __tablename__ = "artigo_tag"

    id_artigo = Column(Integer(), ForeignKey("artigo.id"), primary_key=True, index=True)
    id_tag = Column(Integer(), ForeignKey("tag.id"), primary_key=True, index=True)
