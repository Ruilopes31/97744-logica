import os
os.system("clear")
import time


def verificar (n1,n2):
    media = (n1+n2 )/ 2
    return media

n1 = int(input("digite sua primeira nota:"))
n2 = int(input("digite a segunda nota:"))

media = verificar(n1,n2)

print("calculando a media...")
time.sleep(1)

print(f"sua media é:{media:.2f}")

if media > 7:
    print("aluno aprovado")
else:
    print("aluno reprovado")
        
time.sleep(5)