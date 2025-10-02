import bisect

def lerpalavras (fname):
    lista = []
    with open(fname,"r") as file:
        for line in file:
            line = line.strip()
            if line:
                lista.append(line)
    return lista

x = lerpalavras("wordlist.txt")
print(x)

def funcaobinaria(lista,prefixo):
    start = bisect.bisect_left(lista,prefixo)
    end = bisect.bisect_left(lista,prefixo[:-1]+ chr(ord(prefixo[-1]) + 1))
    return end - start

y = funcaobinaria(x,"ea")
print(y)