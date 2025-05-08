import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome:str
    idade:int
    peso:float
    altura: float

pessoa1 = Pessoa("Alice", 20, 90, 8.0)

print("\n= dados da pessoa =")
print(f"nome:  {pessoa1.nome}, idade: {pessoa1.idade} peso:{pessoa1.peso} altura:{pessoa1.altura} .")





