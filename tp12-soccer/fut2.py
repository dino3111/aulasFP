def lista_clubes(filename):
    resultado = []

    with open(filename, "r", encoding="utf-8") as file:
        next(file) 
        for line in file:
            line = line.strip()

            ranking, nome, pais, score, alteracao, scoreanopassado, subiudesceu = line.split(",")
            resultado.append((int(ranking), nome, pais, int(score), alteracao, scoreanopassado, subiudesceu))
    
    return resultado

def mostrarpais(lista_clubes_data, pais):
    
    for clubes in lista_clubes_data:
        if clubes[2].lower() == pais.lower():
            print(f"{clubes[0]} {clubes[1]} - {clubes[3]}")

def write(lista_clubes_data, pais, ficheirosaida):
    with open(ficheirosaida, "w") as file:
        for clubes in lista_clubes_data:
            if clubes[2].lower() == pais.lower():
                linha = f"{clubes[0]} {clubes[1]} - {clubes[3]}\n"
                file.write(linha)

def dictpais(lista_clubes_data):
    resultado = {}

    for clubes in lista_clubes_data:
        pais = clubes[2]
        clubes = clubes[1]

        if pais not in resultado:
            resultado[pais] = []
        
        resultado[pais].append(clubes)

    return resultado

def subiumais(lista_clubes_data):
    clube_nome = None
    pontos = -1

    for clubes in lista_clubes_data:
        if clubes[6] == "+":
            subida = int(clubes[4])
            if subida > pontos:
                pontos = subida
                clube_nome = clubes[1]
    
    print(clube_nome)

def dadosclubes(lista_clubes, nome):
    encontrado = False

    for clubes in lista_clubes:
        if nome.lower() == clubes[1].lower():
            print(f"Ranking: {clubes[0]}\nNome: {clubes[1]}\nPaís: {clubes[2]}\nScore: {clubes[3]}\nPosições: {clubes[6]}{clubes[4]}\nScore Ano Passado: {clubes[5]}")
            encontrado = True
            break

        if not encontrado:
            print("Erro.")

def mediaporpais(lista_clubes_data, pais):
    pontos = 0
    count = 0

    for clube in lista_clubes_data:
        if pais.lower() == clube[2].lower():
            pontos += int(clube[0])
            count += 1
    
    if count == 0:
        print(f"Não há clubes registados para o país '{pais}'.")

    else:
        media = pontos / count
        print(f"O ranking médio dos clubes de {pais} é {media:.2f}.")



 

def main():
    # Ficheiro de input
    filename = "C:\\Users\\claud\\Desktop\\Estudo FP\\tp12-soccer\\Soccer_Football_Clubs_Ranking.txt"
    
    # Carregar dados
    clubes_data = lista_clubes(filename)

    # Mostrar clubes de Portugal no ecrã
    print("Clubes de Portugal no ecrã:")
    mostrarpais(clubes_data, "Portugal")

    # Escrever os mesmos clubes num ficheiro de saída
    ficheiro_saida = "C:\\Users\\claud\\Desktop\\Estudo FP\\tp12-soccer\\Clubes_Portugal.txt"
    write(clubes_data, "Portugal", ficheiro_saida)
    print(f"\nInformação escrita no ficheiro: {ficheiro_saida}")

    # Criar dicionário de países e clubes
    dicionario_paises = dictpais(clubes_data)
    print("\nDicionário de países e clubes (exemplo):")
    # Mostrar os 5 primeiros países para não imprimir tudo
    for i, (pais, clubes) in enumerate(dicionario_paises.items()):
        print(f"{pais}: {clubes}")
        if i >= 4:
            break

     # Mostrar o clube que mais subiu no ranking
    print("\nClube que mais subiu no ranking:")
    subiumais(clubes_data)

    # 5. Procurar dados de um clube pelo nome
    nome_clube = input("\nDigite o nome de um clube para ver os seus dados: ")
    dadosclubes(clubes_data, nome_clube)

    # 6. Calcular o ranking médio de um país
    pais_media = input("\nDigite o país para calcular o ranking médio dos seus clubes: ")
    mediaporpais(clubes_data, pais_media)

if __name__ == "__main__":
    main()


