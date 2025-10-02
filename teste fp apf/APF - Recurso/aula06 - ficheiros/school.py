# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname,"r") as file:
        next(file)
        for line in file:
            line = line.strip()
            if line:
                dados = line.split('\t')
                numero = int(dados[0])
                nome = dados[1]
                curso = dados[2]
                regime = dados[3]
                data = dados[4]
                nota1 = float(dados[5])
                nota2 = float(dados[6])
                nota3 = float(dados[7])
                lst.append((numero, nome, nota1, nota2, nota3))
    return lst

    
def notafinal(lst):
    for tuplo in lst:
        numero, nome, nota1, nota2, nota3 = tuplo
        nota_final = ( nota1 + nota2 + nota3 ) / 3 
    return nota_final



# c) Crie a função printPauta aqui...
def printPauta(lst):
    print(f"{"Numero":>6} {"Nome":^50} {"Nota":>10}")
    for aluno in lst:
        numero, nome, nota1, nota2, nota3 = aluno
        nota_final = ( nota1 + nota2 + nota3 ) / 3
        print(f"{numero:>6} {nome:^50} {nota_final:>10.01f}")



# d)
def main():
    lst=[]
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    lst.sort()
    printPauta(lst)


# Call main function
if __name__ == "__main__":
    main()


