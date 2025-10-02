# jmr 2024 o programa

import sys

def nascimentomorte_org(date):
    parts = date.split("/") 
    if len(parts) == 3:
        mes = int(parts[0])
        dia = int(parts[1])
        ano = int(parts[2])
        return (ano, mes, dia)
    else:
        return None

def load_lifetimes_file(composers):
    lst = []
    with open(composers, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "" or line[0] == "#":
                continue
            parts = line.split("\t")
            if len(parts) != 3:
                continue
            nascimento = parts[0]
            morte = parts[1]
            nome = parts[2]
            nascimento_org = nascimentomorte_org(nascimento)
            morte_org = nascimentomorte_org(morte)
            if morte_org and nascimento_org:
                line_organizada = [nascimento_org, morte_org, nome]
                lst.append(line_organizada)
    return lst

def calcular_idade(nascimento, morte):
    ano_nasc, mes_nasc, dia_nasc = nascimento
    ano_morte, mes_morte, dia_morte = morte
    idade = ano_morte - ano_nasc
    if (mes_morte, dia_morte) < (mes_nasc, dia_nasc):
        idade -= 1
    return idade


def main():
    file_name = 'composers.txt'  # Replace with your file name
    lifes = load_lifetimes_file(file_name)

    print("THE DEAD COMPOSERS SOCIETY")
    print("==========================")
    print(f"{'Nome':<55} {'Idade':<12} {'Data de Morte':<10}")


    for nascimento, morte, nome in lifes:
        idade = calcular_idade(nascimento, morte)
        data_morte = f"{morte[1]:02}/{morte[2]:02}/{morte[0]}"
        print(f"{nome:<55} {idade:<12} {data_morte:<10}")


if __name__ == "__main__":
    main()

