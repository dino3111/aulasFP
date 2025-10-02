# ==========================================
# ✅ GUIA COMPLETO: LISTAS EM PYTHON
# ==========================================

# 🔹 O que é uma lista?
# É uma coleção ordenada e mutável de elementos. Pode conter diferentes tipos de dados.

exemplo = [1, 2, 3, 4, 5]

# 🔹 Criar listas
vazia = []
numeros = [10, 20, 30]
mistura = [1, "Python", True, 3.14]
lista_com_funcao = list("abc")  # ['a', 'b', 'c']

# 🔹 Acessar elementos
print(numeros[0])       # 10 (primeiro)
print(numeros[-1])      # 30 (último)
print(mistura[1:3])     # ['Python', True] (fatiamento)

# 🔹 Modificar elementos
numeros[1] = 25         # Altera o valor do índice 1
print(numeros)          # [10, 25, 30]

# 🔹 Adicionar elementos
numeros.append(40)      # Adiciona ao fim
numeros.insert(1, 15)   # Insere na posição 1
print(numeros)          # [10, 15, 25, 30, 40]

# 🔹 Remover elementos
numeros.remove(25)      # Remove o valor 25
ultimo = numeros.pop()  # Remove o último e retorna
del numeros[0]          # Remove o índice 0
# numeros.clear()       # Apaga todos os elementos

# 🔹 Iterar sobre lista
for item in exemplo:
    print(item)

# 🔹 Verificar se valor existe
if 3 in exemplo:
    print("3 está na lista.")

# 🔹 Tamanho da lista
print(len(exemplo))     # 5

# 🔹 Ordenar e inverter
lista = [3, 1, 4, 2]
lista.sort()            # Ordena de forma crescente
print(lista)            # [1, 2, 3, 4]
lista.reverse()         # Inverte a ordem
print(lista)            # [4, 3, 2, 1]

# 🔹 Copiar lista
copia = lista.copy()     # Cópia independente
outra = lista[:]         # Outra forma de copiar

# 🔹 Juntar listas
a = [1, 2]
b = [3, 4]
c = a + b                # [1, 2, 3, 4]
a.extend(b)              # a = [1, 2, 3, 4]

# 🔹 Listas aninhadas (nested)
matriz = [
    [1, 2],
    [3, 4]
]
print(matriz[1][0])      # 3

# 🔹 Compreensão de listas (list comprehension)
quadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# 🔹 Funções úteis
print(min(exemplo))      # 1
print(max(exemplo))      # 5
print(sum(exemplo))      # 15

# 🔹 Exemplo prático
frutas = ["maçã", "banana", "laranja"]
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# ==========================================
# ✅ FIM DO GUIA DE LISTAS
# ==========================================

# Podes usar este ficheiro como referência e testar exemplos.
