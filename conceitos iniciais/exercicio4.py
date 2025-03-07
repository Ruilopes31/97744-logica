import os
print.system("clear")

#print solicitando dados para o usúario
 mes_do_ano = int(input("digite um número de 1 a 12:"))


#verificando
match mes_do_ano :

    case 1:
        resultado=janeiro
    case 2:
        resultado = fevereiro
    case 3:
        resultado= março
    case 4:
        resultado=abril
    case 5:
        resultado=maio
    case 6:
        resultado=junho
    case 7:
        resultado=julho
    case 8:
        resultado=agosto
    case 9:
        resultado=setembro
    case 10:
        resultado=outubro
    case 11:
        resultado=novembro
    case 12:
        resultado=dezembro
    case _:
        print("opção inválida")
