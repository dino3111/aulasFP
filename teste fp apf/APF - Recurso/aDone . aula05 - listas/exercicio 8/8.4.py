def positionOfFirstLargest(lista):
   max = lista[0]
   for i in lista[1:]:
      if max < i:
         max = i
   indice_max = lista.index(max)
   return indice_max

x = positionOfFirstLargest([1,2,3,4,5,4,5,3])
print(x)


#SEM INDEX 

def positionOfFirstLargest(lista):
   max = lista[0]
   indice_max = 0
   for i in range(1,len(lista)):
      if max < lista[i]:
         max = lista[i]
         indice_max = i
   return indice_max

Y = positionOfFirstLargest([1,2,3,4,5,4,5,3])
print(Y)