fala = str(input("Fale: "))

while True:
    resp = input(f"Repete: ")
    if resp == "":
        continue
    elif resp != fala:
        break