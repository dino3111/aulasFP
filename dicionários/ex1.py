# The periodic table of elements.
periodicTable = {
    "H": "Hydrogen", "C": "Carbon", "O": "Oxygen",
    "Fe": "Iron", "Au": "Gold", "Na": "Sodium",
    "Ag": "Silver", "Pb": "Lead", "Pu": "Plutonium"
}

def run_lookup():
    while True:
        symbol = input()
        if symbol == "Q":
            break
        elif symbol in periodicTable:
            print(f"{symbol} = {periodicTable[symbol]}")
        else:
            print("Invalid symbol.")

def main():
    """
    Exemplos de input (colar no terminal quando correr o ficheiro):
    O
    Fe
    Xx
    Q

    Esperado:
    O = Oxygen
    Fe = Iron
    Invalid symbol.
    """
    run_lookup()

if __name__ == "__main__":
    main()
