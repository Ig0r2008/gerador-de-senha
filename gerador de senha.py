"""
#<import e from>

"""
import string
from random import choice
from time import sleep
import os, sys
try:
    from tqdm import tqdm
except:
    print('instalando os pacote')
    os.system('pip install tqdm')
    try:os.system('clear')
    except:os.system("cls")
    
import string
from random import choice
import os
def get_password(lenght):
    valores = string.ascii_letters  
    valores += string.digits 
    valores += string.punctuation 
    senha = ""
    for _ in range(lenght):
        senha += choice(valores)
    return senha
def clear_prompt():
    os.system("cls")
while True:
    clear_prompt()
    opt = int(input(f"Escolha a opção\n[1] Gerar a Senha\n ~ $ "))
    if opt == 1:
        clear_prompt()
        lenght = int(input(f"Digite o Tamanho da Senha\n ~ $ "))
        clear_prompt()
        print(f"Senha: {get_password(lenght)}")
        input("[Aperte qualquer tecla para continuar.]")
