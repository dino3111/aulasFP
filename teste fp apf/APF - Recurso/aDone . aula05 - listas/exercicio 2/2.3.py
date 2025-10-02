def minmax(lst):
    max = lst[0]
    min = lst[0]
    for i in lst[1:]:
        if i > max:
            max = i
        if min > i:
            min = i
    return max,min
x = minmax([3,2,2,2,21,2])
print (x)