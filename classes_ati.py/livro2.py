import os
from dataclasses import dataclass
import time
os.system("cls || clear")

@dataclass
class Livro:
    nome:str
    autor:str
    categoria:str
    preco:float

  
    


lista_livro = []

for i in range(3):
    print("escreva o livro:")
    livro = Livro(
        nome= input("Nome:"),
        autor= input("Autor:"),
        categoria = input("Categoria:"),
        preco = input("Preco:")

    )
    lista_livro.append(livro)
    print()


ler_dados_catalogo = "Catalogo_.txt"

print("salvando dados no arquivo.")
with open(ler_dados_catalogo, "a") as arquivo_livro:
    for livro in lista_livro:
        arquivo_livro.write(f"{livro.nome},{livro.autor},{livro.categoria},{livro.preco} \n")
print("salvo com sucesso.")
print("\nAcessando dados em arquivo .")
try:
    with open(ler_dados_catalogo, "r") as arquivo_livro:
        linhas = arquivo_livro.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("o arquivo nao foi encontrado.")

