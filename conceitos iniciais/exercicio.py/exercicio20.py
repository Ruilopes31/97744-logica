import os 

os.system("cls || clear")

# Exemplo de uso do laço de repetição while
idade = int(input("digite sua idade:"))

while idade < 18:
    print("não autorizado. \nSomente maiores de 18. \n")
    idade = int(input("digite sua idade:"))
print("acesso permitido.")
print("fim.")