import os
os.system("clear")

# Listas para armazenar os dados
contador = 0
soma_salario = 0
maior_idade = 0
menor_idade= 9999
mulheres5k = 0

while True:
    
    print("""
codigo | descricao
  1    | adicionar pessoa
  2    | exibir resultados
  3    | sair
""")
    opcao = int(input("digite a opcao desejada:"))
      
    match opcao :
        case 1:
            idade = int(input("informe a idade:"))
            sexo= input("informe os sexo com M/F:").upper()
            salario = float(input("informe o salario:"))
            contador += 1
            soma_salario += salario

            if idade  > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
            
            if sexo == "f" and salario >= 5000:
                mulheres5k += 1
            os.system("cls || clear")
        case 2 :
              if contador >0:
                media_salario_grupo = soma_salario / contador
                print("\n= exibindo resultados =")
                print(f"media de salario do grupo: {media_salario_grupo}")
                print(f"maior idade do grupo: {maior_idade}")
                print(f"menor idade do grupo: {menor_idade}")
                print(f" quantidade mulheres com salario a aprtir de 5 mil : {mulheres5k}")
              else:
                 print("nao existem dados para exibir.")

              time.sleep(3)
              os.system("cls || clear")
        case 3:
              print("\nFim do programa.")
              break
        case _:
            print("\nOpcao invalida.")
            time.sleep(3)
            os.system("cls || clear"
                        )
       
    