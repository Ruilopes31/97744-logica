import os

os.system("clear")


#solicitando dados

login_correto= "rui lopes"
senha_correta= "123456"

# solicita login e senha do usuario

login= input("digite seu login:")
senha= input("digite sua senha:")

if login == login_correto and senha == senha_correta:
    print("Bem vindo!")
else :
    print("login ou senha invalidos")
