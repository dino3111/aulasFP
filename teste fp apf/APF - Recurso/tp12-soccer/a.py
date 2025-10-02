def infoclube(fname):
    with open(fname, "r") as file:
        next(file)
        lista = []
        for line in file:
            line = line.strip()
            if line:
                info = line.split(",")
                pos = int(info[0])
                nome = info[1]
                pais = info[2]
                score = int(info[3])
                subida = int(info[4])
                score_anoanterior = int(info[5])
                indicacao = info[6]
                lista.append((pos,nome,pais,score,subida,score_anoanterior,indicacao))
    return lista

def nome_pais(pais):
    lista = infoclube("clubes.csv")
    lista_clubes = [(info[0], info[1], info[3]) for info in lista if info[2] == pais]
    return lista_clubes

def escreverf (fname,pais):
    lista_clubes = nome_pais(pais)
    with open(fname, "w") as file:
        for i in lista_clubes:
            file.write(f"{i[0]},{i[1]},{i[2]}")

def dicionario(lista,fname):
    lista = infoclube(fname)
    dic = {}
    for info in lista:
        pais = info[2]
        nome = info[1]
        if pais not in dic:
            dic[pais]=set()
            dic[pais].add(nome)
        elif pais in dic:
            dic[pais].add(nome)
    return dic

def rankingup (lista,fname):
    lista = infoclube(fname)
    max = lista[0][0]
    for info in lista:
        ranking = info[0]
        nome = info[1]
        pais = info[2]
        score = int(info[3])
        subida = int(info[4])
        score_anoanterior = int(info[5])
        indicacao = info[6]    
        if ranking > max:
            max = ranking
    return ((ranking,nome,pais,score,subida,score_anoanterior,indicacao))

def nome_clube (nome,lista,fname):
    lista = infoclube(fname)
    nome = (input("qual é o clube que deseja procurar?"))
    nome = nome.lower()
    for info in lista:
        ranking = info[0]
        pais = info[2]
        score = int(info[3])
        subida = int(info[4])
        score_anoanterior = int(info[5])
        indicacao = info[6] 
        nome_clube = lista[1].lower()
        if nome == nome_clube:
            print(f"Clube: {nome_clube} Ranking: {ranking} País: {pais} Score: {score} Subida ou descida no ranking: {subida} Score ano anterior: {score_anoanterior} Indicação se subiu ou desceu no ranking (+ ou -): {indicacao} ")
        elif nome not in lista:
            print("ERRO!")
        
def rankingmedio(lista,fname):
    lista = infoclube(fname)
    pais_ranking = {}
    pais_clubes = {}
    for info in lista:
        ranking = info[0]
        pais = info[2]
        if pais not in pais_ranking:
            pais_ranking[pais]=ranking
            pais_clubes[pais]=1
        else:
            pais_ranking[pais] += ranking
            pais_clubes[pais] += 1

    for pais in pais_ranking:
        media = pais_ranking[pais] / pais_clubes[pais]
        pais_ranking[pais] = media
    paisordenado = sorted(pais_ranking.items(), key= lambda x: x[1])
    for pais in paisordenado:
        print(f"{pais} (ranking médio) : {media}")

def menu():
    print("\nMenu:")
    print("1. Listar clubes de um país")
    print("2. Guardar clubes de um país num ficheiro")
    print("3. Criar dicionário de países e clubes")
    print("4. Encontrar clube com maior ranking")
    print("5. Procurar clube por nome")
    print("6. Calcular ranking médio dos países")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            pais = input("Digite o nome do país: ")
            clubes = nome_pais(pais)
            for clube in clubes:
                print(f"{clube[0]}, {clube[1]}, {clube[2]}")
        elif opcao == '2':
            pais = input("Digite o nome do país: ")
            output_filename = input("Digite o nome do ficheiro de output: ")
            escreverf(output_filename, pais)
            print(f"Informação escrita no ficheiro {output_filename}")
        elif opcao == '3':
            dic = dicionario()
            for pais, clubes in dic.items():
                print(f"{pais}: {', '.join(clubes)}")
        elif opcao == '4':
            clube = rankingup()
            print(f"Clube com maior ranking: {clube}")
        elif opcao == '5':
            nome = input("Digite o nome do clube: ")
            nome_clube(nome)
        elif opcao == '6':
            rankingmedio()
        elif opcao == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()











        






