import os
os.system("clear")


soma_pares = 0
soma_total = 0
quant_pares = 0
quant_impares = 0
total_numeros = 0

while True:
    numero = int(input("digite um numero inteiro positivo (o para sair):"))
    
    if numero == 0:
        break
    if numero > 0:
        total_numeros += 1
        soma_total += numero
        if numero %2 == 0:
            quant_pares += 1
            soma_pares += numero
        else:
            quant_impares += 1
    else:
        print("pro favor , digite apenas numeros inteioros positivos.")

if quant_pares >0 :
    media_pares = soma_pares / quant_pares
else:
    media_pares = 0

if total_numeros >0:
    media_geral = soma_total / total_numeros
else:
    media_geral = 0

print(f"Quantidade de numeros pares:{quant_pares:.2f}")
print(f"quantidade de numeros impares:{quant_impares:.2f} ")
print(f"media de valores pares:{media_pares :.2f}")
print(f"media geral dos numeros lidos:{media_geral:.2f} ")
