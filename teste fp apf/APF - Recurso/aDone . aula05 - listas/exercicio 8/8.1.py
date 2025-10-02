def evenThenOdd(string):
   novastring = ""
   for i in range(len(string)):
      if i % 2 == 0:
         novastring = novastring + string[i]
   for i in range(len(string)):
      if i % 2 != 0:
         novastring = novastring + string[i]
   return novastring

x = evenThenOdd('AaBbCcDdEeFf')
print(x)