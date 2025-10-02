def criarabreviadas(nome):
    abreviada = ""
    for i in nome:
        if i.isupper() == True:
            abreviada = abreviada + i
    return abreviada

x = criarabreviadas("Universidade de Aveiro")
print(x)
y = criarabreviadas("United Nations Organization")
print(y)