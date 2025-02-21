import os

os.system("clear")

#solicita dois numeros do usuario

num1= float(input("digite o primeiro número:"))
num2 = float(input("digite o segundo número:"))

#calcule os resultados
media =(num1+num2)/ 2
soma =num1+num2
produto =num1*num2
menor = min(num1, num2)
maior = max(num1, num2)


#exibir na tela os resultados
print(" média :",media)
print("soma:", soma)
print("produto:", produto)
print("menor:", menor)
print("maior:", maior)



