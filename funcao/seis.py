import os 
os.system(" cls || clear")
import time
par_impar = []
quantidade= 6

print("= par e impar= ")
for i in range(quantidade):
    item = int(input(f"digite o {i+1}º numero:"))
    par_impar.append(item)


par= 0 
impar= 0

for numero in par_impar:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print("\nnumeros:", par_impar)
print(f"analisando os numeros...")
time.sleep(5)
print(f"quantidade de numeros pares:{par}")
print(f"quantidade de numeros impares:{impar}")

