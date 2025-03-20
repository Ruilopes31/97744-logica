import os 

os.system("cls || clear")

# solicitar nota do usuario
usuario= "rui" \
senha= "froes"

while True :
    usuario= input("digite o usuario:")
    senha = input("digite sua senha:")
    
   if usuario == usuario and senha == senha: 
       print("Bem Vindo !!")
       break
   
    else:
      print(" acesso negado. \nTente novamnete\n")