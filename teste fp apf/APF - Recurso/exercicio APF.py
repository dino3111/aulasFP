def loadfile(filename):
    with open(filename,"r") as file:
        next(file)
        lista = []
        for line in file:
            line = line.strip()
            if line:
                info = line.split(",")
                nome = info[0]
                continente = info[1]
                area = int(info[2])
                population =int(info[3])
                lista.append((nome,continente,area,population))
    return lista