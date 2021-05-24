# for n in range(2,10):
#     print(n,"---")
#     for x in range(2,n):
#         print(n,x,">>>")
#         if n%x == 0:
#             print(n," es igual a",x, " * ", n/x)
#             break

#     else :
#         print(n, "es un numero primo")
import random
lista=[]
con=1

while(con<=4):
   
    a=(3)*random.random()
    lista.append(a)
    
    con+=1
print(lista)
    