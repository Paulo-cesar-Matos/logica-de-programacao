import os
import subprocess

mai = 0
pesadao = ""

def limpar_tela ():
    tela = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(tela, shell=True)

def exibir_tela():
    print(f'''D E T E C T O R   D E   P E S A D O''')

for i in range(1, 3):
    limpar_tela()
    exibir_tela()
    nome = str(input("Digite o nome: "))
    peso = int(input(f"Digite o peso de {nome}: "))
    mai = peso
    if i == 1 or peso > mai:
        mai = peso
        pesadao = nome
    print(f"Maior peso até agora: {peso}kg")
    input("\nPressione Enter para contunuar...")

limpar_tela()
exibir_tela()

# e é mt mais pesado q seu pai kkkkk