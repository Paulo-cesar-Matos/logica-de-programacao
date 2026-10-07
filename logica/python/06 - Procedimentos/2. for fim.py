import time
num = int(input("Digite um valor: "))
for c in range(1, 99):
    time.sleep(1)
    print(f"{num} x {c} = {num * c}")
print("A soma dos valores de 1 a 10 é: ", sum(range(1, 99)))