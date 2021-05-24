# for i in range(1,11,2):
#     a=i*10
#     print(i," X 10 =",(i*10))
# for i in range(1,11):    
#     print(2*i)
def nombre(frase):
    for i in frase:
        print(i, end=", ")

def run():
    a=input("ingrese una frase: " )
    nombre(a.upper())


if __name__=='__main__':
    run()