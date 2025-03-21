import os

# Limpando o terminal
os.system("clear")

# Inicializando variáveis
soma_notas = 0  # Armazena a soma das notas
contador = 0  # Conta quantas notas foram inseridas

while True:
    nota = float(input("Digite uma nota: "))  # Solicita a nota ao usuário
    soma_notas += nota  # Soma a nota inserida
    contador += 1  # Incrementa o contador
    
    resposta = input("Deseja inserir outra nota? (s/n): ").strip().lower()  # Pergunta se deseja continuar
    if resposta == 'n':  # Se a resposta for 'n', encerra o loop
        break

# Calculando a média
media = soma_notas / contador

# Exibindo o resultado
print(f"A média das {contador} notas inseridas é: {media:.2f}")
