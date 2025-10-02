
def parseMDY(date):
    parts = date.split("/") 
    if len(parts) == 3:
        mes = int(parts[0])
        dia = int(parts[1])
        ano = int(parts[2])
    elif len(parts) == 1:
        ano = int(parts[0])
        dia = 0
        mes = 0
    return (ano, mes, dia)


def yearsBetween(date1, date2):
    anos = date2[0] - date1[0]
    if date2[1] < date1[1]:
        anos = anos - 1
    return anos



def main():
    # Test parseMDY
    print(f"{parseMDY('12/25/2024') = }")  # (2024, 12, 25)
    print(f"{parseMDY('4/25/1974') = }")   # (1974, 4, 25)
    print(f"{parseMDY('1755') = }")        # (1755, 0, 0)

    # Test yearsBetween
    print(f"{yearsBetween((1900, 6, 1), (1935, 5, 31)) = }")  # 34
    print(f"{yearsBetween((1900, 6, 1), (1935, 6, 1)) = }")   # 35
    print(f"{yearsBetween((1900, 6, 1), (1936, 5, 31)) = }")  # 35


# This program may be used as a module too
if __name__ == "__main__":
    main()

