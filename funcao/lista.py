import os
os.system("cls || clear")

lista_notas = [] # criando uma lista

for i in  range(quantidade_notas)
    nota = float(input("digite uma nota:"))
    lista_notas.append(nota)
    
media = sum(lista_notas) / quantidade_notas

if media >= 7:
    resultado = "aprovado"
elif media >= 5 :
    resultado = "recuperacao"
else:
    resultado = "reprovado"
    
print()
for nota in lista_notas: #ForEach
    print(f"nota:{nota}")
    
    
print()
print(f)
