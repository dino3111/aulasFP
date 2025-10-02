# Complete este programa como pedido no guião da aula.

def listContacts(contacts):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:<12s} : {}".format("Numero", "Nome"))
    for num in contacts:
        print("{:<12s} : {}".format(num, contacts[num]))

def filterPartName(contacts):
    partName = input("nome parcial?")
    partName = partName.lower()
    lista_numeros = {}
    for numero, nome in contacts.items():
        if partName in nome.lower():
            lista_numeros[numero] = nome
            print(f"{nome} - {numero}")
    return lista_numeros

def adicionar(contacts):
    numero = input("qual é o numero que deseja adicionar?")
    nome = input("nome do numero ?")
    contacts[numero] = nome
    print(f"Contacto {nome} adicionado com sucesso.")

def remover(contacts):
    numero = input("que numero deseja eliminar?")
    numeros = contacts.keys()
    if numero not in numeros:
        print("o numero não está registado!")
    elif numero in numeros:
        del contacts[numero]
        print("numero apagado com sucesso!")

def procurarnumero(contacts):
    numero = input("que numero deseja procurar?")
    numeros = contacts.keys()
    if numero not in numeros:
        print("o numero não está registado!")
    elif numero in numeros:
        nome = contacts.get(numero)
        print(f"o numero que acabaste de procurar é do {nome}")
        

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
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            adicionar(contactos)
        elif op == "R":
            remover(contactos)
        elif op == "N":
            procurarnumero(contactos)
        elif op == "P":
            filterPartName(contactos)
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

