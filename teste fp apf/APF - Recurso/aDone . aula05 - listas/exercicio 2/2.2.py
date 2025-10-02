def countlower(lst,v):
    count = 0
    for i in lst:
        if i < v:
            count += 1
    return count

x = countlower([6,6,6,1,5],7)
print(x)