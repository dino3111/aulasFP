def contarvotos():

    votosA = 0
    votosB = 0
    votosNulos = 0

    while True:
        a = input("Introduz um voto A, B e END para terminar: ").upper().strip()

        if a == "A":
            votosA += 1
        elif a == "B":
            votosB += 1
        elif a == "END":
            break
        else:
            votosNulos += 1
    
    votostotal = votosB + votosA
    percentagem_a = (votosA*100) / votostotal
    percentagem_b = (votosB*100) / votostotal
    print(f"Nulos: {votosNulos}")
    print(f"A: {percentagem_a}")
    print(f"B: {percentagem_b}")

contarvotos()

