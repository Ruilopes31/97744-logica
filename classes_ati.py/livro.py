import os
from dataclasses import dataclass

os.system('cls || clear') 

@dataclass
class Autor:
    nome : str
    biografia: str


@dataclass
class livro:
    titulo: str
    ano: int
    autor: Autor

QUANTIDADE_LIVRO = 1
QUANTIDADE_AUTOR = 1

lista_autor = []
lista_livro= []

print("cadastro de Autor")
for i in range(QUANTIDADE_AUTOR):
    autor= Autor(
        nome = input("Nome do autor:"),
        biografia =input("Biografia:")
    )
    lista_autor.append(autor)
    print()

print("Cadastro de Livro")
for i in range(QUANTIDADE_LIVRO):
    titulo = input(f"Título do livro : ")
    ano = int(input("Ano de publicação: "))


print(" Salvando os dados dos clientes =")
nome_arquivo = "dados_clientes.txt"

with open(nome_arquivo, "w") as arquivo:
  for linha in lista_clientes:
  arquivo.write(f"()")
