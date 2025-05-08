import os
from dataclasses import dataclass
import time
os.system("cls || clear")

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
    
@dataclass
class Pessoa:
    nome:str
    endereco: Endereco
    email:str

    print("estamos enfrentando problemas , por favor aguarde ...")
    time.sleep(5)
    print("estamos de volta , seus dados irão aparecer automaticamente")
    time.sleep(2)

    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"\nemail: {self.email}")
        print(f"Endereço: {self.endereco.logradouro}, numero: {self.endereco.numero}")

endereco1 = Endereco(" rua lula", 13)
pessoa1 = Pessoa("rui", , endereco1)
pessoa1.exibir_dados()

print()
endereco2 = Endereco("rua bolsonaro",22)
pessoa2 = Pessoa("camila", 17, endereco2)
pessoa2.exibir_dados()

print("estamos confirmando seus dados, espere ...")
time.sleep(5)
print("obrigado por sua colaboracao")


print()






