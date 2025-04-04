import os
os.system("cls || clear")
import time


def inflacao(preco):
    if preco < 100:
       valor = preco * 1.10
      
    else:
          valor = preco * 1.20
    return valor 
    
    

preco = float(input("digite o preco do produto:"))

preco_final = inflacao(preco)


print(f"acrescentando...")
time.sleep(3)
print(f"o preco total é:{preco_final}")








              