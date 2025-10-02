def inputfloatlist():
    lista_nova = []
    while True:
        x = (input("que numero deseja?"))
        if x == "":
            break
        else:
            lista_nova.append(int(x))
    return lista_nova

numeros = inputfloatlist()
print("Lista final:", numeros)
