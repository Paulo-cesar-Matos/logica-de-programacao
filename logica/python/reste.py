import os
import subprocess

def exibir_tela():
    print('''D E T E C T O R   D E   P E S A D O''')
    
def limpar_tela():
    tela = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(tela, shell=True)

# Inicializamos as variáveis de controle fora do loop
maior_peso = 0
pesadao = ""

for i in range(1, 6):  # Ajustado para 5 pessoas (de 1 a 5)
    limpar_tela()
    exibir_tela()
    
    nome = str(input("Digite o nome: "))
    peso = int(input(f"Digite o peso de {nome}: "))
    
    # Na primeira volta, ou se o peso atual for maior que o recordista anterior:
    if i == 1 or peso > maior_peso:
        maior_peso = peso
        pesadao = nome
        
    print(f"Maior peso até agora: {maior_peso} kg (pertencente a {pesadao})")
    input("\nPressione Enter para continuar...") # Pausa para conseguir ler antes de limpar a tela

# Resultado final após as 5 pessoas
limpar_tela()
exibir_tela()
print(f"A pessoa mais pesada é {pesadao} com {maior_peso} kg.")