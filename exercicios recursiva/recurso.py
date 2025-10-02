def separar(palavra):
    
    if len(palavra) == 1:
        return palavra
    
    return palavra[0] + "-" + separar(palavra[1:])

# Teste
print(separar("ola"))  # o-l-a
print(separar("python"))  # p-y-t-h-o-n
