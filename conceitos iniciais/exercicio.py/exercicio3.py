import os

os.system("clear")

# solicitando dados para o usuario
primeiro_numero = int(input(" digite o primeiro número:"))
segundo_numero= int(input("digite o segundo número:"))
terceiro_numero = int(input("digite o terceiro número:"))


# verificando o maior e menor 
print(f"os números informados foram: {primeiro_numero}, {segundo_numero} e {terceiro_numero}")

# determinar maior e do menor número
maior = max(primeiro_numero,segundo_numero,terceiro_numero)
menor= min(primeiro_numero,segundo_numero,terceiro_numero)

# exibe o maior e menor número

print(f"maior número :{maior}")
print(f"menor número:{menor}")
