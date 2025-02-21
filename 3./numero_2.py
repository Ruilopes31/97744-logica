import os

os.system("clear")

#solicita dois numeros do usuario

num1= int(input("digite o primeiro número:"))
num2 = int(input("digite o segundo número:"))

#calcule os resultados

soma = num1 + num2
produto = num1 * num2
media =(num1+num2)/ 2

menor = min(num1,num2)
maior = max(num1,num2)


#exibir na tela os resultados
print(" média :",media)
print("soma:", soma)
print("produto:", produto)
print("menor:", menor)
print("maior:", maior)

if  num1 == num2:
    print(f" os números são iguais")
else:
    print(f" maior númro: {maior numero}")
    print(f"menor número:{}")





