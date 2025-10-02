# ==========================================
# ✅ GUIA COMPLETO: DICIONÁRIOS EM PYTHON
# ==========================================

# 🔹 O que é um dicionário?
# É uma coleção de pares chave:valor. As chaves são únicas.

exemplo = {
    "nome": "João",
    "idade": 25,
    "cidade": "Lisboa"
}

# 🔹 Criar dicionários
aluno = {"nome": "Ana", "nota": 18}
aluno2 = dict(nome="Carlos", nota=15)
vazio = {}

# 🔹 Acessar valores
print(aluno["nome"])         # Ana
print(aluno.get("nota"))     # 18
print(aluno.get("curso"))    # None (não dá erro)

# 🔹 Modificar ou adicionar elementos
aluno["nota"] = 20           # Modifica
aluno["curso"] = "Python"    # Adiciona

# 🔹 Remover elementos
aluno.pop("curso")           # Remove chave 'curso'
del aluno["nota"]            # Também remove
# aluno.clear()              # Apaga tudo (comentado para não apagar)

# 🔹 Iterar sobre o dicionário
for chave in exemplo:
    print(chave, exemplo[chave])

for chave, valor in exemplo.items():
    print(f"{chave} = {valor}")

# 🔹 Métodos úteis
print(exemplo.keys())        # dict_keys(['nome', 'idade', 'cidade'])
print(exemplo.values())      # dict_values(['João', 25, 'Lisboa'])
print(exemplo.items())       # dict_items([('nome', 'João'), ...])

# 🔹 Verificar se chave existe
if "nome" in exemplo:
    print("Chave 'nome' existe.")

# 🔹 Dicionários aninhados (nested)
alunos = {
    "joao": {"nota": 15, "curso": "Python"},
    "maria": {"nota": 18, "curso": "Java"}
}
print(alunos["joao"]["nota"])  # 15

# 🔹 Exemplo prático:
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "profissao": "Engenheiro"
}
pessoa["idade"] += 1
pessoa["cidade"] = "Porto"

# 🔹 Output formatado
for k, v in pessoa.items():
    print(f"{k}: {v}")

# 🔹 Dica: usar get() evita erros se a chave não existir
print(pessoa.get("telefone", "Não existe"))

# ==========================================
# ✅ FIM DO GUIA DE DICIONÁRIOS
# ==========================================

# Podes usar este ficheiro como referência e testar exemplos.
