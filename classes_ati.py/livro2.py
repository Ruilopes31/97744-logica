import os
from dataclasses import dataclass
import time
os.system("cls || clear")

@dataclass
class livro:
    nome:str
    autor:str
    categoria:str
    preco:float


QUANTIDADE_LIVRO = 3
lista_livro= []

print("catalogo_livros.txt")
for i in range(QUANTIDADE_LIVRO):