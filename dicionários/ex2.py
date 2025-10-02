capitais = {
    "Portugal": "Lisboa",
    "França": "Paris",
    "Espanha": "Madrid",
    "Itália": "Roma",
    "Alemanha": "Berlim"
}

def run_lookup():
    while True:
        pais = input()

        if pais == "Q":
            break
        elif pais in capitais:
            print(f"{pais} = {capitais[pais]}")
        else:
            print("Invalid Country.")

def main():
    """
    Exemplos de input:
    Portugal
    Itália
    Brasil
    Q

    Esperado:
    Portugal = Lisboa
    Itália = Roma
    Invalid country.
    """
    run_lookup()

if __name__ == "__main__":
    main()
