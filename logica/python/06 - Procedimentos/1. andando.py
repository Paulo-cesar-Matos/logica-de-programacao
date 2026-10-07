import time
resposta = (input("Posso andar? [S/N] "))

if resposta.lower() == "s":
    for i in range(99999999999999999999999):
        print(f"Andando os passos {i + 1}")
        time.sleep(1)
else:
    print("Seu alajado >:-(")