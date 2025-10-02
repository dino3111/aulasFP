def stockholders(portfolios):
    dic = {}
    for nome, carteira in portfolios.items():
        for empresa, montante in carteira.items():
            if empresa not in dic:
                dic[empresa] = set()
                dic[empresa].add(nome)
            dic[empresa].add(nome)
    return dic

