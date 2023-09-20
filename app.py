from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Produto
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Redireciona automaticamente para a tela do swagger")
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")

@app.get('/', tags=[home_tag])
def home():
   
    return redirect('/openapi/swagger#')

@app.post('/cadastrar_produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: ProdutoSchema):
    
    produto = Produto(
        nome=form.nome,
        quantidade=form.quantidade,
        valor=form.valor)
    try:
        session = Session()
        session.add(produto)
        session.commit()
        return apresenta_produto(produto), 200

    except IntegrityError as e:
        error_msg = "Produto de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400


@app.get('/produtos', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
   
    session = Session()
    produtos = session.query(Produto).all()

    if not produtos:
        return {"produtos": []}, 200
    else:
        print(produtos)
        return apresenta_produtos(produtos), 200


@app.get('/busca_produto', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
   
    produto_id = query.id
    session = Session()
    produto = session.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        error_msg = "Produto não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:
        return apresenta_produto(produto), 200


@app.delete('/deleta_produto', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    
    produto_id = query.id
    session = Session()
    count = session.query(Produto).filter(Produto.id == produto_id).delete()
    session.commit()

    if count:
        return {"mesage": "Produto removido", "id": produto_id}
    else:
        error_msg = "Produto não encontrado na base :/"
        return {"mesage": error_msg}, 404