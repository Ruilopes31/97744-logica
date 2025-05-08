def calcular_combustivel():
    try:
        distancia = float(input("Digite a distância em KM: "))
        consumo = float(input("Digite o consumo do veículo (KM/L): "))
        preco = float(input("Digite o preço do litro do combustível (R$): "))

        litros = distancia / consumo
        valor_total = litros * preco

        print("\n🚗💨 Resultado do cálculo:")
        print(f"Distância percorrida: {distancia:.2f} km")
        print(f"Litros necessários: {litros:.2f} L")
        print(f"Custo total estimado: R$ {valor_total:.2f}\n")

    except ValueError:
        print("\n❌ Erro: Por favor, insira apenas números válidos.\n")

# Executar a função
calcular_combustivel()
