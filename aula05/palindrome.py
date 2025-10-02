def ispalindrome(s):
    for i in range(len(s)):
        if s[i] != s[-(i+1)]:
            return False
    return True

a = input("Introduz uma palavra: ")
print(ispalindrome(a))