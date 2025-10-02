# Complete este programa como pedido no guião da aula.

def listContacts(contacts):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12} : {:^30} : {:<30}".format("Numero", "Nome", "Morada"))
    for num, (nome, morada) in contacts.items():
        print("{:>12} : {:^30} : {:<30}".format(num, nome, morada))

def filterPartName(contacts):
    """Returns a new dict with the contacts whose names contain partName."""
    partName = input("nome parcial? ").lower()
    filtered_contacts = {num: (name, address) for num, (name, address) in contacts.items() if partName in name.lower()}
    return filtered_contacts

def adicionar(contacts):
    """Adds a new contact to the dictionary."""
    numero = input("qual é o numero que deseja adicionar? ")
    nome = input("nome do numero? ")
    morada = input("morada do contacto? ")
    contacts[numero] = (nome, morada)
    print(f"Contacto {nome} adicionado com sucesso.")

def remover(contacts):
    """Removes a contact from the dictionary."""
    numero = input("que numero deseja eliminar? ")
    if numero in contacts:
        del contacts[numero]
        print(f"Contacto {numero} removido com sucesso.")
    else:
        print("o numero não está registado!")

def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)ista de contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op

def main():
    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ("Universidade de Aveiro","Santiago, Aveiro"),
        "727392822": ("Cristiano Aveiro","Viseu"),
        "387719992": ("Maria Matos","Porto"),
        "887555987": ("Marta Maia","Algarve"),
        "876111333": ("Carlos Martins","Porto"),
        "433162999": ("Ana Bacalhau","Lisboa")
        }
    while True:
        op = menu()
        if op == 'L':
            listContacts(contactos)
        elif op == 'A':
            adicionar(contactos)
        elif op == 'R':
            remover(contactos)
        elif op == 'N':
            num = input("Número a procurar? ")
            if num in contactos:
                nome, morada = contactos[num]
                print(f"{num} : {nome} : {morada}")
            else:
                print(f"Contacto {num} não encontrado.")
        elif op == 'P':
            filtered = filterPartName(contactos)
            listContacts(filtered)
        elif op == 'T':
            print("Terminar.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()