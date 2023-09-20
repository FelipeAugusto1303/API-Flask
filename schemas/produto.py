from pydantic import BaseModel
from typing import Optional, List
from model.produto import Produto



class ProdutoSchema(BaseModel):
    nome: str = "Banana Prata"
    descricao: str = "A banana prata é um alimento muito nutritivo rico em potassio"
    quantidade: Optional[int] = 12
    valor: float = 12.50


class ProdutoBuscaSchema(BaseModel):
    id: int = 1


class ListagemProdutosSchema(BaseModel):
    
    produtos:List[ProdutoSchema]


def apresenta_produtos(produtos: List[Produto]):
    
    result = []
    for produto in produtos:
        result.append({
            "id": produto.id,
            "nome": produto.nome,
            "quantidade": produto.quantidade,
            "valor": produto.valor,
        })

    return {"produtos": result}


class ProdutoViewSchema(BaseModel):
    
    id: int = 1
    nome: str = "Banana Prata"
    descricao: str = "A banana prata é um alimento nutritivo rico em potassio"
    quantidade: Optional[int] = 12
    valor: float = 12.50


class ProdutoDelSchema(BaseModel):
    id: int

def apresenta_produto(produto: Produto):
   
    return {
        "id": produto.id,
        "nome": produto.nome,
        "quantidade": produto.quantidade,
        "valor": produto.valor
    }

def mostra_produto(produto: Produto):

    return {
        "id": produto.id,
        "nome": produto.nome,
        "descricao": produto.descricao,
        "quantidade": produto.quantidade,
        "valor": produto.valor
    }
    
