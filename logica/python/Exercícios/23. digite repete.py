num = int(input("Digite um número para repetir: "))
cont = 1
totN = 0
while cont <= num:
    n = int (input("Digite um número: "))
    cont = cont + 1
    if n < 0:
        totN = totN + 1
cont = cont + 1
print(f"Foram digitados {totN} valores negativos!")