# def letra(*l):
    
#     for a in l:
#         print("Hola ",a)

# def main():
#     letra("juan","gerson","pablo")

# if __name__=='__main__':
#      main()

# def intro(**data):
#     print("El tipo de dato es ",type(data))
#     print(data.items())
#     for a,b in data.items():
#         print("su ",a," es ",b)


# intro(nombre="juan",apellido="cardenas",DNI=7737382)

def factorial1(n):
    f=1
    for a in range(1,n+1):
        f=f*a
       
    print(f)

def factorial2(n):
    if(n>1):
        f=n* factorial2(n-1)
        return f
    else:
        return 1

def run():
    x=3
    factorial1(x)
  
    print (factorial2(x))

if __name__=='__main__':
    run()