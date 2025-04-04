import os
os.system("cls || clear")

def somar(n1, n2):
    calcular = n1 + n2
    return calcular

def subtrair(n1, n2):
    calcular = n1 - n2
    return calcular

n1 = int(input("digite o primeiro numero:"))
n2 = int(input("digite o segundo numero:"))


soma= somar(n1,n2)
subtracao = subtrair(n1,n2)

print(f"soma: {soma}")
print(f"subtracao: {subtracao}")
