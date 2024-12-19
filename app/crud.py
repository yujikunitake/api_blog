from datetime import datetime
from sqlalchemy.orm import Session
from . import models


# Retorna todos os artigos, pode ser filtrado por intervalo de data de publicação e tag
def retorna_artigos(db:Session, data_publicaco_inicial: datetime = None, data_publicacao_final: datetime = None, tags: list[str] = None):
    query = db.query(models.Artigo).join(models.Artigo.tags)

    # Filtra por data, se fornecida
    if data_publicaco_inicial and data_publicacao_final:
        query = query.filter(models.Artigo.data_publicacao.between(data_publicaco_inicial, data_publicacao_final))
    elif data_publicaco_inicial:
        query = query.filter(models.Artigo.data_publicacao >= data_publicaco_inicial)
    elif data_publicacao_final:
        query = query.filter(models.Artigo.data_publicacao <= data_publicacao_final)

    # Filtra por tags, se fornecidas
    if tags:
        query = query.filter(models.Tag.descricao.in_(tags))

    # Ordena os artigos por data de publicação decrescente
    query = query.order_by(models.Artigo.data_publicacao.desc())

    return query.all()

# Retorna o artigo de acordo com o ID fornecido
def retorna_artigo_por_id(db: Session, id_artigo: int):
    return db.query(models.Artigo).filter(models.Artigo.id == id_artigo).first()

# Insere um novo artigo no banco, recebe o título, contúdo e, opcionalmente, uma ou mais tags. 
def cria_artigo(db: Session, titulo: str, conteudo: str, tags: list[str]):
    db_artigo = models.Artigo(titulo=titulo, conteudo=conteudo)

    # Itera sobre a lista de tags fornecida e verifica se as tags fornecidas existem no banco.
    lista_tags = []
    for descricao_tag in tags:
        tag = db.query(models.Tag).filter(models.Tag.descricao == descricao_tag).first()
        # Se a descrição da tag não existir no banco, a mesma será criada.
        if not tag:
            tag = models.Tag(descricao=descricao_tag)
            db.add(tag)
        lista_tags.append(tag)

    db_artigo.tags = lista_tags

    db.add(db_artigo)
    db.commit()
    db.refresh(db_artigo)

    return db_artigo
