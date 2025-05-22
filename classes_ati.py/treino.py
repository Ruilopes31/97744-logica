import os
from dataclasses import dataclass
os.system("cls || clear")


@dataclass
class Produto:
    nome:str
    preco:str
    categoria:str
    codigo:str

class Fornecedor:
    nome:str
    cnpj:str
    contato:str

lista_produto=[]
lista_fornecedor=[]

for i in range():
    print("digite os dados do produto:")
    produto = Produto(
        nome = input("Nome:"),
        admissao = input("Preco:"),
        matricula = input("Categoria:"),
        endereco = input("Codigo:")
    )
    lista_produto.append(produto)
    print()
