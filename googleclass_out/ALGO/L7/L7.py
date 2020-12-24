# задача 1
import string, random
def generator() :
  arr = []
  a = string.ascii_uppercase + string.ascii_lowercase + string.digits
  for i in range (len (a)) :
    arr.append( a [i] )
  print(random.sample(arr, 10))
generator()

# задача 2
def convert(str):
    return (str[0].split())
 
str = ['Heute ist ein schöner Tag am Himmel fliegen bunte Drachen']
encoded = convert(str)
hash = [ 4 , 'k' , 's' , 'a' , 1 , 'I' , 'S' , 'S' , 'h' , 0 ]
for i in zip(encoded, hash):
   print(i)
 
