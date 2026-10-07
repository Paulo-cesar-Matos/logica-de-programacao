print("Somador")
cont_num = int(input("Quantos números serão contados? "))
soma = 0
cont = 1

while cont <= cont_num:
    valor = int (input(f"Digite o {cont}° valor: "))
    soma += valor
    cont += 1
print(f"A soma de todos os valores é: {soma}")