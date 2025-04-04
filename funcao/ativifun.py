import os
os.system("clear")
import time


def calcular_media(n1, n2):
    return (n1+n2) / 2


n1 = float(input("digite a primeiro nota:"))
n2 = float(input("digite a segunda nota:"))

    #  media
media = calcular_media(n1,n2)

print(f"calculando a media...")
time.sleep(5)
print(f"a media do aluno é:{media:.2f}")
