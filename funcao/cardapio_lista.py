# limpando o terminal
import os

# Limpando o terminal
os.system("clear")

# Cardápio do restaurante
menu = {
    1: ("Picanha", 25),
    2: ("Lasanha", 20),
    3: ("Strogonoff", 18),
    4: ("Bife acebolado", 15),
    5: ("Pão com ovo", 5)
}

# solicitando dados para o usuario
print("""

================== MENU ====================

Código \tPrato \t\tValor  
1   \t\tPicanha \t\t25,00  
2  \t\tLasanha \t\t20,00  
3  \t\tStrongonoff \t\t18,00  
4   \t\tBIfe acebolado \t\t15,00  
5   \t\tPão com ovo \t\t5,00  
""")
# Coletando pedidos
pedidos = []
total = 0


while True :
   
    opcao = int(input("digite a opção desejada:"))
    
    if opcao in menu:
        pedidos.append(menu[opcao])
        total += menu[opcao][1]
        print(f"{menu[opcao][0]} adicionado ao pedido.")
          
    else:
        print("Opção inválida. Tente novamente.")
    
    resposta = input("Deseja escolher outro prato? (s/n): ").strip().lower()
    if resposta != 's':
            break


    # exibindo resultados.
print()
print(f"prato: {prato}")
print(f"valor: R$ {valor:.2f}")