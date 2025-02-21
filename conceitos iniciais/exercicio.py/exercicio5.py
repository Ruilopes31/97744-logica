# limpando o terminal
import os
os.system("clear")

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

opcao = int(input("digite a opção desejada:"))


# verificando.

match opcao:
    case 1:
        prato="picanha"
        valor=25
    case 2:
        prato="lasanha"
        valor=20
    case 3:
        prato="strongonoff"
        valor=18
    case 4:
        prato="bife acebolado"
        valor=15
    case 5:
        prato="pão com ovo"
        valor=5
    case _:
        prato="opção inválida"
        valor= 0

# exibindo resultados.
print()
print(f"prato: {prato}")
print(f"valor: R$ {valor:.2f}")