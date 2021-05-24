# def es_primo(a):
#     contador=0
#     for i in range(1,a+1):
#         if(i==1 or i==a):
#             continue
#         elif(a%i==0):
#             contador +=1
#     if (contador==0):
#         return True
#     else:
#         return False


# def run():
#     num=int(input('ingrese un numero: '))
#     if es_primo(num):
#         print("es numero primo ")
#     else:
#         print("no es numero primo")

# if (__name__=='__main__'):
#     run()
def esprimo(num):
    a=0
    contador=0
    while(contador<=num):
        contador+=1;
        if(contador==1 or contador==num):
            continue
        elif(num%contador==0):
            a+=1     
        
    if(a==0):
        return True
    else:
        return False


def run():
    num=int(input("ingrese un numero: "))
    if(esprimo(num)):
        print("es primo :V")
    else:
        print("no es primo :,V")


if __name__=='__main__':
    run()