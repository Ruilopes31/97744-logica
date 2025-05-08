import os
os.system("cls || clear")
import time

def calcular (peso,altura):
    imc = peso / altura * altura
    return imc



imc = calcular(peso,altura)

if imc <18.5:
    print("abaixo do peso")
elif imc >= 18.5 or imc <24.9:
    print("peso normal")
elif imc >=25 or imc < 29.9:
    print("sobrepeso")
elif imc >= 30 or imc < 34.9:
    print("obesidade 1 grau")
elif imc >=35 or imc < 39.9:
    print("obesidade 2 grau")
elif imc >=40:
    print("obesidade 3 grau")
    
peso=int(input(" digite seu peso em (kg):"))
altura = int(input("digite sua altura em (m): "))  
    
    
    







print(f"calculando seu imc...")
print(f"seu imc é:{imc:.2f}")    
time.sleep(1)


