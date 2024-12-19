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

# Listagem de Artigos
@app.get("/artigos/")
def listar_artigos(data_publicacao_inicial: datetime = None, data_publicacao_final: datetime = None, tag: str = None, db: Session = Depends(get_db)):
    return crud.retorna_artigos(db=db, data_publicaco_inicial=data_publicacao_inicial, data_publicacao_final=data_publicacao_final, tag=tag)

# Exibição de Artigo Único
@app.get("/artigos/{id}")
def exibir_artigo_unico(id: int, db: Session = Depends(get_db)):
    return crud.retorna_artigo_por_id(db=db, id_artigo=id)

# Publicação de Artigo
@app.post("/artigos/")
def publicar_artigo(artigo: schemas.ArtigoPublicacao, db: Session = Depends(get_db)):
    return crud.cria_artigo(db=db, titulo=artigo.titulo, conteudo=artigo.conteudo, tag=artigo.tag)
