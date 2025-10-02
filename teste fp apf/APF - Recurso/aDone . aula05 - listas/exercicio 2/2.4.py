def valor_medio(lst):
    max = lst[0]
    min = lst[0]
    for i in lst[1:]:
        if i > max:
            max = i
        if min > i:
            min = i
    vm = (max + min ) // 2
    count = 0
    for i in lst:
        if i < vm:
            count += 1
    return vm,count
x = valor_medio([1,2,4,5,5,6,7,7,8,8,19])
print(x)