class fracciones:

    def __init__(self,num,den):
        if isinstance(num,int):
            self.num=num
        else:
            self.num=0

        if isinstance(den,int) and (den!=0):
            self.den = den
        else:
            self.den=1
    
    def __str__(self):
        return "{"+str(self.num)+"/"+str(self.den)+"}"
    def __mul__(self, t):
        n=self.num* t.num
        d=self.den* t.den
        x=fracciones(n,d)
        return x
        
    def __add__(self, a):
        n=(self.num*a.den)+(a.num*self.den)
        d=(self.den*a.den)
        r=fracciones(n,d)
        return r

    def __eq__(self,b):
         if(self.num/self.den)== (b.num/b.den):
             print("ambas fracciones son iguales")
             return True
         else:
             return False

    # def ingresar(self):
    #      n=int(input("ingrese un numero de la fraccion N°: ",j))
    #      m=int(input("ingrese otro numero de la fraccion N°:  ",j))
    #      r=fracciones(n,m)
    #      return r
    #     #  r=fracciones(n,m)
    #     #  return r

def main():
    n=int(input("ingrese el denominador de la fraccion N°1: "))
    m=int(input("ingrese el numerador de la fraccion N°1:  "))
    
    a=fracciones(n,m)
    print(a)

    n=int(input("ingrese el denominadorde la fraccion N°2: "))
    m=int(input("ingrese el numerador de la fraccion N°2:  "))
    b=fracciones(n,m)
    print(b)

    print(a==b)

    print("multiplicacion ")
    r=a*b
    print(r)

    print("suma ")
    r=a+b
    print(r)


if __name__=='__main__':
    main()