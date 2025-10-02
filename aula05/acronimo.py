def shorten(str):
    novastring = ""

    for i in range(len(str)):
        if str[i].isupper():
            novastring += str[i]

    return novastring

a = input("Introduz um nome para obteres o acrónimo: ")
print(shorten(a))

