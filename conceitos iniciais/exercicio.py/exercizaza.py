import os
os.system("clear")

idade = []
salarios = []
mulher_salario = []

while True :

     print("MENU:")
     print("1 - adicionar pessoa")
     print("2- exibir resultados")
     print("3- sair")

     opcao = input("escolher uma opcao:")

     if opcao ='1':
     idade = int(input("Informe a idade: "))
     sexo = input("Informe o sexo (M/F): ").strip().upper()
     salario = float(input("Informe o salário: R$ "))           