def reapeatNumTimes(n):
   lista_nova = []
   for i in range(1,n+1):
      lista_nova.extend([i]*i)  
   return lista_nova

x = reapeatNumTimes(4)
print (x)