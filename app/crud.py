from datetime import datetime
from sqlalchemy.orm import Session
from . import models


# Retorna todos os artigos, pode ser filtrado por intervalo de data de publicação e tag
def retorna_artigos(db:Session, data_publicaco_inicial: datetime = None, data_publicacao_final: datetime = None, tag: str = None):
    query = db.query(models.Artigo)

    # Filtra por data, se fornecida
    if data_publicaco_inicial and data_publicacao_final:
        query = query.filter(models.Artigo.data_publicacao.between(data_publicaco_inicial, data_publicacao_final))
    elif data_publicaco_inicial:
        query = query.filter(models.Artigo.data_publicacao >= data_publicaco_inicial)
    elif data_publicacao_final:
        query = query.filter(models.Artigo.data_publicacao <= data_publicacao_final)

    # Filtra por tag, se fornecida
    if tag:
        query = query.filter(models.Artigo.tag == tag)

    # Ordena os artigos por data de publicação decrescente
    query = query.order_by(models.Artigo.data_publicacao.desc())

    return query.all()

# Retorna o artigo de acordo com o ID fornecido
def retorna_artigo_por_id(db: Session, id_artigo: int):
    return db.query(models.Artigo).filter(models.Artigo.id == id_artigo).first()

# Insere um novo artigo no banco, recebe o título, contúdo e, opcionalmente, uma tag. 
def cria_artigo(db: Session, titulo: str, conteudo: str, tag: str = None):
    db_artigo = models.Artigo(titulo=titulo, conteudo=conteudo, tag=tag)

    db.add(db_artigo)
    db.commit()
    db.refresh(db_artigo)

    return db_artigo
