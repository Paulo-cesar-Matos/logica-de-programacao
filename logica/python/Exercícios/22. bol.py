import time
repe = int(input("Digite o número de repetições: "))
multi = int(input("Digite o número de multiplicações: "))
cont = 0

while cont < repe:
    cont = cont + 1
    resul = cont * multi
    print(f"{cont} x {repe} = {resul}")
    time.sleep(1)