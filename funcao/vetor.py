import os 
os.system("cls || clear")



lista_de_numeral = []
quantidade = 5


print("= lista de numeral = ")
for i in range(quantidade):
    item = (input(f"digite o {i+1}º numero da lista:"))
    lista_de_numeral.append(item)

print("\nNUMEROS DA LISTA:", lista_de_numeral)


maior= max(lista_de_numeral)
menor= min(lista_de_numeral)

print(f"maior numero: {maior}")
print(f"menor numero: {menor}")