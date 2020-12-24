# задача 1
from numpy import zeros, dot, savetxt
from numpy.linalg import norm

def cosine_distance(u, v):
   return 1.0 - (dot(u, v) / (norm(u) * norm(v)))

if __name__ == "__main__":
# подгружаем файл, в котором будем искать наши строчки
   with open("text.txt") as f:
      
       lines = sum(1 for _ in f)
       f.seek(0)
      
       import re
       slova = {}
      
       lcount, wcount = 0, 0
       for line in f:
          
           p = re.compile(r"[^a-z]+")
           tokens = p.split(line.lower())
          
           tokens.pop()
           for token in tokens:
              
               if token not in slova:
                   slova[token] = {
                       "index": wcount,
                       "occurrences": [0] * lines
                   }
                   wcount += 1
              
               elif slova[token]["occurrences"][lcount] != 0:
                   continue
              
                  
               slova[token]["occurrences"][lcount] = tokens.count(token)   
           lcount += 1
      
     
       arr = zeros((lines, len(words)))
      
# ищем проявления
       for slovo in slova:
           i, j = 0, slova[slovo]["index"]
           for occ in slova[slovo]["occurrences"]:
               arr[i, j] = occ
               i += 1
# Cравниваем...
       dist = []
       u = arr[0,]
       for j in range(1, lines):
           v = arr[i,]
           dist.append({"index": j, "distance": cosine_distance(u, v)})   
      
       dist.sort(key=lambda x: x["distance"])
# печатаем самые ближайшие к первому строчки
       print("%d %d" % (
           dist[0]["index"],
           dist[1]["index"],
       ))

# задача 2
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def f(x):
    return np.sin(0.2 * x) * np.exp(0.1 * x) + 5 * np.exp(0.5 * (-x))

I = [[1,1**1,1**2,1**3], [1,4**1,4**2,4**3],[1,10**1,10**2,10**3],[1,15**1,15**2,15**3]]
matrix = np.array (I)
i = [f(1.),f(4.),f(10.),f(15.)]
res = np.linalg.solve(I, i)

def f3(x):
    return res[0] + res[1] + res[2] + res[3]*x

print (res)

fig, ax = plt.subplots()
x = np.arange(1, 15, 0.1)
ax.plot(x, f(x), color="black", label= "Функция от Х")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()
