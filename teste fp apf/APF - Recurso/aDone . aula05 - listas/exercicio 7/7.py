def ispalindorme(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
x = ispalindorme("radar")
print(x)
y = ispalindorme("121")
print(y)
z = ispalindorme("123")
print (z)
