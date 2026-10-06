num = int (input("Digite um número para repetir: "))
cont = 1
totN = 0
while cont <= num:
    n = int (input(f"Digite o {cont}° número: "))
    if n < 0:
        totN += 1
    cont += 1
print(f"Foram digitados {totN} valores negativos!")