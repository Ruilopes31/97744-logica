import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Funcionario:
    nome:str
    admissao:str
    matricula:str
    endereco:str

@dataclass
class Cliente:
    nome:str
    nascimento:str
    endereco:str

lista_funcionario=[]
lista_cliente = []

for i in range(3):
    print("digite os dados do funcionario:")
    funcionario = Funcionario(
        nome = input("Nome:"),
        admissao = input("Admissao:"),
        matricula = input("Matricula:"),
        endereco = input("Endereco:")
    )
    
    lista_funcionario.append(funcionario)
    print()

for i in range(3):
    print("digite os dados do cliente:")
    cliente = Cliente(
        nome = input("Nome:"),
        nascimento = input("Nascimento:"),
        endereco = input("Endereco:")

    )
    lista_cliente.append(cliente)
    print()


nome_arquivo = "dados_funcionario.txt"
nome_arquivo2 = "dados_cliente.txt"

print("salvando dados no arquivo.")
with open(nome_arquivo, "a") as arquivo_funcionario:
    for funcionario in lista_funcionario:
        arquivo_funcionario.write(f"{funcionario.nome},{funcionario.admissao},{funcionario.matricula},{funcionario.endereco} \n")


print("salvando dados no arquivo.")
with open(nome_arquivo2, "a") as arquivo_cliente:
    for cliente in lista_cliente:
        arquivo_cliente.write(f"{cliente.nome},{cliente.nascimento},{cliente.endereco} \n")
print("salvo com sucesso.")
print("\nAcessando dados em arquivo .")
try:
    with open(nome_arquivo, "r") as arquivo_funcionario:
        linhas = arquivo_funcionario.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("o arquivo nao foi encontrado.")
try:
    with open(nome_arquivo2, "r") as arquivo_cliente:
        linhas = arquivo_cliente.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("o arquivo nao foi encontrado.")
