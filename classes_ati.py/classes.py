import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class pessoa:
    nome:str
    idade:int
    

@dataclass
class Pet:
    nome:str
    idade:int
    peso: float
    altura :float

pessoa1 = pessoa("Alice", 20)
pessoa2 = pessoa("bob", 30)

pet1 = Pet("toto", 4 , 7.8)
pet2 = Pet("tubarao", 6 , 9.2)

print("\n= dados da pessoa =")
print(f"nome:  {pessoa1.nome}, idade: {pessoa1.idade} .")
print(f"nome:  {pessoa2.nome}, idade: {pessoa2.idade} .")

print("\n= dados do pet =")
print(f"nome:  {pet1.nome}, idade: {pet1.idade} peso:{pet1.peso} .")
print(f"nome:  {pet2.nome}, idade: { pet2.idade} peso:{pet2.peso} altura: {} .")



