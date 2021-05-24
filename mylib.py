
from random import random

def generaAleatorios(cantNumeros, ini, fin):    
    lista=[]
    ind=0
    while ind<cantNumeros:
        val = ini + (fin - ini) * random()  
        lista.append(val)
        ind+=1
    return lista

def tablaMulti(n):
    i=1
    while i<=10:
        print(n," * ", i, " = ", n*i)
        i+=1

def main():
    n = int(input("Cuantos numeros deseas: "))
    ini = int(input("Inicio de rango: "))
    fin = int(input("Final de rango: "))
    print( generaAleatorios(n,ini,fin) )
    tablaMulti(n)