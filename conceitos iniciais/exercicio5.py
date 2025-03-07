import os

os.system("clear")

#solicitando dados para o usuario

dia=int(input("digite um número de 1 a 7 1para representar un dia da semana:"))


#verifica se o dia é valido ou invalido

if dia == 1 or dia == 7:
    print("final de semana")
elif 2 <= dia <= 6:
    print("dia útil")
else:
    print("inválido")    
        
