import os
os.system("clear")
import time

def calcular_media (n1, n2,n3):
    calcular = (n1+ n2 + n3) / 3
    return calcular


n1 = int(input("digite sua primeira nota:"))
n2 = int(input("digite a segunda nota:"))
n3 = int(input("digite sua terceira nota:"))


media = calcular_media( n1, n2, n3)
print(f"calculando a media...")
print(f"sua media é:{media:.2f}")
time.sleep(5)