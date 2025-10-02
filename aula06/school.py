# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, "r") as file:
        next(file)
        for line in file:
            line = line.strip()
            numero, nome, curso, regime, dataincricao, nota1, nota2, nota3 = line.split("\t")
            aluno = (int(numero), nome, float(nota1), float(nota2), float(nota3))
            lst.append(aluno)

    return lst
    
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    return (reg[2] + reg[3] + reg[4]) / 3

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print(f"{'Numero':>6}   {'Nome':^40}   {'Nota':>6}")
    print("-" * 60)

    for aluno in lst:
        numero = aluno[0]
        nome = aluno[1]
        notafinal = notaFinal(aluno)

        print(f"{numero:>6}   {nome:^40}   {notafinal:>6.1f}")


# d)
def main():
    lst = []
    # ler os três ficheiros
    loadFile("C:\\Users\\claud\\Desktop\\Estudo FP\\aula06\\school1.csv", lst)
    loadFile("C:\\Users\\claud\\Desktop\\Estudo FP\\aula06\\school2.csv", lst)
    loadFile("C:\\Users\\claud\\Desktop\\Estudo FP\\aula06\\school3.csv", lst)
    
    # ordenar a lista por número do aluno
    lst.sort(key=lambda aluno: aluno[0])
    
    # mostrar a pauta
    printPauta(lst)



# Call main function
if __name__ == "__main__":
    main()


