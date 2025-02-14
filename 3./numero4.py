import os

os.system("clear")

#solicita notas do usuario

numero 1= float(input("digite o primeira numero:"))
numero 2 = float(input("digite o segundo numero:"))

#calcule a media
media=(numero1+numero2)/2
soma=(numero1+numero2)
produto=(numero1*numero2)
menor_valor()


#exibir na tela a media
print("sua media é:")


#se esta aprovado ou não

if media< 7:
    print("o aluno esta REPROVADO")
else print("o aluno esta APROVADO")
