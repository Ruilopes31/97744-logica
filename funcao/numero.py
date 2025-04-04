import os
os.system("cls || clear")
import time
def verificar(numero):
    if numero> 0:
        print("o numero e posititvo.")
    elif numero < 0:
        print("o numero e negativo.")

    else: 
        print("o numero é neutro")



print("verificando se um numero e positivo ou negativo.")
numero = int(input("digite um numero:"))
time.sleep(5)
verificar(numero)
