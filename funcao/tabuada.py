import os
os.system("cls || clear")
def tabuada():
    os.system("cls || clear")


def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

print("=== TABUADA ===")
numero=int(input("escolha um numero de 1 a 10:"))

tabuada(numero)
