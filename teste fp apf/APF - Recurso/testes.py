for i in range(1, 6):
    print(i, end=" + ") 

print("Olá", "mundo", "Python", sep="-")


# Lista de tuplos
dados = [(1, 3, 2), (2, 2, 5), (3, 3, 1), (4, 2, 1)]

# Ordenar primeiro por x[1] e depois por x[2]
ordenado = sorted(dados, key=lambda x: x[2]/x[1] , reverse=True)

print(ordenado)
# Output: [(4, 2, 1), (2, 2, 5), (3, 3, 1), (1, 3, 2)]


lista = [1,2,3,4,1,3,6,3,2,9,0,1]
lisa_ordenada = sorted (lista, reverse=True)
print(lisa_ordenada)

L = ["Mario", "Carla","anabela", "Maria", "nuno"]

print(sorted(L))
print(sorted(L, reverse=True))
print(sorted(L, key=len))
print(sorted(L,key = lambda x: (len(x),x)))
print(sorted(L, key=lambda x: x))
print(L[0].casefold())


def triangulos(n):
    if n == 1:
        return 1
    return (n*2)-1 + triangulos(n-1)

x = triangulos(4)
print(x)

abreviada = "rada"
abreviada2 = abreviada + "r"
print(abreviada2)

dados = {"nome": "Alice", "idade": 25, "cidade": "Lisboa"}
x = dados.keys()
print(x)