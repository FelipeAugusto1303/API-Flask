from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    descricao = Column(String(300))
    quantidade = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, descricao:str, quantidade:int, valor:float,
                 data_insercao:Union[DateTime, None] = None):
        
        self.nome = nome
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor = valor

        
        if data_insercao:
            self.data_insercao = data_insercao


