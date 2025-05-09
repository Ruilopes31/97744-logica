import os
from dataclasses import dataclass

os.system('cls || clear') 

@dataclass
class Clientes:
    nome: str
    email:str
    telefone: str

lista_clientes = []
QUANTIDADE_CLIENTES = 2


print("informe os dados do cliente:")
for i in range(QUANTIDADE_CLIENTES):
    cliente =  Clientes(
        nome= input("Nome: "),
        email=input("e-mail:"),
        telefone= input("Telefone:")
    )
    lista_clientes.append(cliente)
    print()


print("\n= Exibindo dados clientes:")
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"e-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")
    print()