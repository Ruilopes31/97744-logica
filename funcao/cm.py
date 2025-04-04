import os
os.system("cls || clear")
import time
def calcular_cm(metro):
    return (metro) * 100

metro = float(input("digite um valor em metros:"))


cm = calcular_cm(metro)

print(f"transformando em cm...")
time.sleep(4)
print(f"o resultado em centimetros é :{metro * 100:.2f}")
