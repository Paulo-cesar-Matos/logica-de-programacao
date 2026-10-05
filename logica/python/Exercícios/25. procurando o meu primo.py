num = int(input("Digite o número do seu primo: "))
c = 1
contDiv = 0
while c <= num:
    if num % c == 0:
        contDiv += 1
    c += 1
    print(c, end=" ")
print(f"Ao todo existem {contDiv} valores divisíveis por {num}")