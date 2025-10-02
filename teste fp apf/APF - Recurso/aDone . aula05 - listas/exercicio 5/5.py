def countDigits(string):
   count = 0
   for i in string:
      if i.isdigit() == True:
         count += 1
   return count

x = countDigits("23 mil 456")
print(x)