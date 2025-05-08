import os
from dataclasses import dataclass
import time
os.system("cls || clear")

@dataclass
class Pessoa:
    nome:str
    idade:int
    peso:float
    altura: float

print("estamos enfrentando problemas , por favor aguarde ...")
time.sleep(5)
print("estamos de volta , pode digitar seus dados")

pessoa1 = Pessoa(

    nome = input("digite seu nome:"),
    idade =int(input("digite sua idade:")),
    peso= float(input("digite seu peso:")),
    altura= float(input("digite sua altura:"))
    )
print("estamos confirmando seus dados, espere ...")
time.sleep(5)
print("obrigado por sua colaboracao")


print()






