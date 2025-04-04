import os
os.system("cls || clear")
from datetime import datetime
import time


def data_nascimento(nascimento):
    return datetime.now().year - nascimento


nascimento = int(input("digite seu ano de nascimento:"))

idade= data_nascimento(nascimento)
print(f"calculando sua idade...")
time.sleep(3)
print(f"idade:{idade}")
