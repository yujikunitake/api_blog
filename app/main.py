from datetime import datetime
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, database, schemas


app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/artigos/")
def publicar_artigo(artigo: schemas.ArtigoPublicacao, db: Session = Depends(get_db)):
    return crud.cria_artigo(db=db, titulo=artigo.titulo, conteudo=artigo.conteudo, tags=artigo.tags)

@app.get("/artigos/")
def listar_artigos(data_publicacao_inicial: datetime = None, data_publicacao_final: datetime = None, tags: list[str] = None, db: Session = Depends(get_db)):
    return crud.retorna_artigos(db=db, data_publicaco_inicial=data_publicacao_inicial, data_publicacao_final=data_publicacao_final, tags=tags)
