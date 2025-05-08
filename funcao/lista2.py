import os
os.system("cls || clear")

lista_de_compras = []
quantidade = 3


print("= lista de compras = ")
for i in range(quantidade):
    item = input(f"digite o {i+1}º item para lista:")
    lista_de_compras.append(item)



print("\n= itens da lista =")
for i, item in enumerate(lista_de_compras,start=1):
    print(f"{i}º item: {item}")