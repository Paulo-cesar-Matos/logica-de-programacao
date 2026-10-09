tot010 = 0
SImp = 0
for c in range(1, 7):
    valor = int(input ("Digite um valor: "))
    if valor >= 0 and valor <= 10:
        tot010 = tot010 + 1
        if valor % 2 == 1:
            SImp = SImp + 1

print(f'''Ao todo foram {tot010} valores entre 0 e 10
    Nesse intervalo, a soma de impares foi de {SImp}''')
