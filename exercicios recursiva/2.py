def soma(n):

    if n == 1:
        return 1

    else:
        return n + soma(n-1)

print(soma(5)) 