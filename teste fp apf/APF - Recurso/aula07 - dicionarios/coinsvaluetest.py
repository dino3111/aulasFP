def value(bag):
    total = 0
    for valor, quantidade in bag.items():
        valor1 = valor * quantidade
        total = total + valor1
    return total

x = {1:7, 5:2, 20:4, 100:1}
print(value(x))
y = {}
print(value(y))# NICEEE