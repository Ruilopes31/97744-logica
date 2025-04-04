import os

os.system("cls || clear")


# funcao sem retorno
# defiindo caracteristica da funcao
def disciplina(nome):
    print(f"ola {nome}! bem vindo ao curso de DS!")

nome= input("digite seu nome:")
nome_disciplina = input("digite o nome da disciplina:")

saudacao(nome) # chamando a funcao
disciplina(nome_disciplina) # chamando a funcao