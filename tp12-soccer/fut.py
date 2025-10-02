def ficheiro(excel):
    equipa = []
    with open(excel, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            partes = line.split(",")
            for i in range(len(partes)):
                partes[i] = partes[i].strip()
            equipa.append(tuple(partes))
    
    return equipa

def pais(lista_clubes, pais):
    for clube in lista_clubes:
        if clube[2].lower() == pais.lower():
             print(f"Ranking: {clube[0]} + {clube[1]} + {clube[3]}")

def clubes_por_pais_ficheiro(lista_clubes, pais, ficheiro_saida):
    with open(ficheiro_saida, "w", encoding="utf-8") as f:
        for clube in lista_clubes:
            if clube[2].lower() == pais.lower():
                linha = f"Ranking: {clube[0]}, Clube: {clube[1]}, Score atual: {clube[3]}\n"
                f.write(linha)

def clubes_dicionario(lista_clubes):
    paises = {}

    for clube in lista_clubes:
        pais = clube[2]
        nome_clube = clube[1]
        if pais not in paises:
            paises[pais] = []
        paises[pais].append(nome_clube)

    return paises 

def clube_mais_subiu(lista_clubes):
    mais_subiu = None
    max_subida = -1

    for clube in lista_clubes:
        posicao = int(clube[4])
        simbolo = clube[6]

        if simbolo == "+" and posicao > max_subida:
            max_subida = posicao
            mais_subiu = clube

    return mais_subiu

def informacao(nome, lista_clubes):
    encontrado = False
    for clube in lista_clubes:
        if clube[1].lower() == nome.lower(): 
            print(f"\nRanking: {clube[0]}")
            print(f"Clube: {clube[1]}")
            print(f"País: {clube[2]}")
            print(f"Score atual: {clube[3]}")
            print(f"Variação: {clube[4]} posições ({'subiu' if clube[6] == '+' else 'desceu'})")
            print(f"Score anterior: {clube[5]}")
            encontrado = True
            break

    if not encontrado:
        print("Erro, introduz o nome válido.")

# Uma função que determine o ranking médio de cada um dos países e o apresente no
# ecrã (o ranking médio determina-se somando o ranking de todos os clubes de um
# dado país e dividindo pelo número de clubes desse país.

def rankmedio(pais, lista_clubes):
    media = 0
    somaranking = 0
    contagem = 0

    for clube in lista_clubes:
        if clube[2].lower() == pais.lower():
            contagem += 1
            somaranking += int(clube[0])
    
    if contagem == 0:
        print("Introduz um país válido.")

    else:
        media = somaranking/contagem
        print(f"Ranking de {pais} = {media}")

    return media

# Altere a função anterior de forma a que imprima os países por ordem crescente do
# ranking médio obtido

def ordemcrescente(lista_clubes):
    ranking_paises = {}
    medias = {}
    
    for clube in lista_clubes:
        pais = clube[2]
        ranking = int(clube[0])

        if pais not in ranking_paises:
            ranking_paises[pais] = {"soma": 0, "contagem": 0}

        ranking_paises[pais]["soma"] += ranking
        ranking_paises[pais]["contagem"] += 1

    for pais, valores in ranking_paises.items():
        soma = valores["soma"]
        contagem = valores["contagem"]  
        media = soma / contagem
        medias[pais] = media

    ordenados = sorted(medias.items(), key=lambda x: x[1])

    print("\nRanking médio por país (ordem crescente):")
    for pais, media in ordenados:
        print(f"{pais}: {media:.2f}")

    return ordenados 


def main():
    # Lê o ficheiro e cria a lista de tuplos
    lista_clubes = ficheiro("C:\\Users\\claud\\Desktop\\Estudo FP\\tp12-soccer\\Soccer_Football_Clubs_Ranking.csv")
    
    # Mostra no ecrã os clubes de Portugal
    print("Clubes de Portugal no ecrã:")
    pais(lista_clubes, "Portugal")
    
    # Escreve a mesma informação num ficheiro de saída
    clubes_por_pais_ficheiro(lista_clubes, "Portugal", "C:\\Users\\claud\\Desktop\\Estudo FP\\tp12-soccer\\portugal_clubes.txt")
    print("\nA informação dos clubes de Portugal foi escrita em 'portugal_clubes.txt'")
    
    # Cria dicionário de países -> lista de clubes
    dicionario = clubes_dicionario(lista_clubes)
    print("\nClubes por país (primeiros 3 países):")
    for i, (pais_nome, clubes) in enumerate(dicionario.items()):
        print(f"{pais_nome}: {clubes}")
        if i == 2:  # só mostra os 3 primeiros para não encher demasiado
            break

    # Clube que mais subiu no ranking
    clube_top = clube_mais_subiu(lista_clubes)
    print("\nClube que mais subiu no ranking:")
    print(f"{clube_top[1]} ({clube_top[2]}) subiu {clube_top[4]} posições, está agora no ranking {clube_top[0]}.")

    informacao("AaB", lista_clubes)
    informacao("Porto", lista_clubes)  # se não existir no ficheiro

    rankmedio("Portugal", lista_clubes)
    rankmedio("Germany", lista_clubes)
    rankmedio("PaísInventado", lista_clubes)

    ordemcrescente(lista_clubes)





# Executa o main
main()


