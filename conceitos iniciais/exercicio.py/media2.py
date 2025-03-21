import os
os.system("clear")

soma=0
contador=0

print("digite um numero inteiro")

while True:
    numero = int(input("digite um numero:"))

    if numero < 0:
        break

    soma += numero
    contador+= 1

if contador >0:
    media = soma/ contador
    print(f"\nA media dos numeros informados : {media:.2f}")
else:
    print("\nNenhum numero informada")