def nomes(names):
    with open(names, "r") as file:
        next(file)
        dic = {}
        for line in file:
            line = line.strip()
            if line:
                line = line.split(" ")
                first_name = line[0]
                last_name = line[-1]
                if last_name not in dic:
                    dic[last_name] = set()
                    dic[last_name].add(first_name)
                dic[last_name].add(first_name)
    return dic


def printcerto(dic):
    for last_name, first_name in x.items():
        print(f"{last_name} : {first_name}")

x = nomes("names.txt")
printcerto(x)

