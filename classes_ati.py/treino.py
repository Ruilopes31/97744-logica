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

for i in range(1):
    print("digite os dados do produto:")
    produto = Produto(
        nome = input("Nome:"),
        preco=  input("Preco:"),
        categoria = input("Categoria:"),
        codigo= input("Codigo:")
    )
    lista_produto.append(produto)
    print() 

for i in range(1):
    print("digite os dados do fornecedor:")
    fornecedor = Fornecedor(
        nome = input("Nome:"),
        cnpj = input("Cnpj:"),
        contato = input("Contato:")
    )
    lista_fornecedor.append(fornecedor)
    print() 

nome_arquivo = "dados_produto.txt"
nome_arquivo2 = "dados_fornecedor.txt"

print("salvando dados no arquivo.")
with open(nome_arquivo, "a") as arquivo_produto:
    for produto in lista_produto:
        arquivo_produto.write(f"{produto.nome},{produto.preco},{produto.categoria},{produto.codigo} \n")


print("salvando dados no arquivo.")
with open(nome_arquivo2, "a") as arquivo_fornecedor:
    for fornecedor in lista_fornecedor:
        arquivo_fornecedor.write(f"{fornecedor.nome},{fornecedor.cnpj},{fornecedor.contato} \n")
print("salvo com sucesso.")
print("\nAcessando dados em arquivo .")
try:
    with open(nome_arquivo, "r") as arquivo_produto:
        linhas = arquivo_produto.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("o arquivo nao foi encontrado.")
try:
    with open(nome_arquivo2, "r") as arquivo_fornecedor:
        linhas = arquivo_fornecedor.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("o arquivo nao foi encontrado.")
