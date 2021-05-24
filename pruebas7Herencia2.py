class A:
    def __init__(self):
        print("soy la clase A")
    def a(self):
        print("Este metodo lo heredo de A")

class B():
    def __init__(self):
        print("Soy la clase B")
    def b(self):
        print("Este metodo lo heredo de B")

class C(A,B):
    def __init__(self):
        print("Soy la clase C")
    def c(self):
        print("Este metodo es C")
x=C()
x.a()
x.c() 
x.b()
print(issubclass(B,C))#B ES UNA SUBCLASE DE C-> FALSE
print(isinstance(x,C))#x es una instancia de la clase C(osea se crep en la clase C)
