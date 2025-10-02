def inputFloatList():
    lista = []
    while True:
        a = input("Introduz um número para a lista: ")
        if a == "":
            break
        try:
            numero = float(a)
            lista.append(numero)
        except ValueError:
            print("Erro.")
    return lista

def countLower(lst, v):
    count = 0
    for i in lst:
        if i < v:
            count += 1
    return count

def minmax(lst):

    minimo = lst[0]
    maximo = lst[0]

    for i in range(len(lst)):
        if lst[i] < minimo:
            minimo = lst[i]
        if lst[i] > maximo:
            maximo = lst[i]

    print(f"Mínimo = {minimo} e Máximo = {maximo}")
    return maximo, minimo

def numeros(maximo, minimo, lst):
    medio = (maximo+minimo)/2

    count2 = 0
    for i in lst:
        if i < medio:
            count2 += 1
    
    print(f"O número médio é {medio} e são {count2} números inferiores.")
    return count2


# a)
valores = inputFloatList()   
print(valores)

# b)
while True:
    vinput = input("Introduz um número, para ver quantos números da lista são inferiores: ")
    try:
        v = float(vinput)
        break
    except ValueError:
        print("Erro, introduz um número válido.")

contagem = countLower(valores, v)
print(contagem)

# c)
maximo, minimo = minmax(valores)
print(maximo, minimo)

# d)
alinead = numeros(maximo, minimo, valores)