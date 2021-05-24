
def run():
        num_1=int(input("ingrese el primer numero: "))
        num_2=int(input("ingrese el segundo numero: "))
        num_3=int(input("ingrese el tercer numero: "))

        while(num_1==num_2 or num_1==num_3 or num_2==num_3 or num_3==num_1):
            print("ERROR UNO DE LOS NUMEROS QUE INGRESO SON IGUALES\nPOR FAVOR VUELVA A DIGITAR LOS NUMEROS: ")
        
            num_1=int(input("ingrese el primer numero: "))
            num_2=int(input("ingrese el segundo numero: "))
            num_3=int(input("ingrese el tercer numero: "))   
            
        
        if(num_1>num_2):
            for i in range(num_1,num_2,-1):
                if(num_1==i):
                    print(num_1,"---> primer numero ingresado....")
                    continue
                print(i)
            if(num_2>num_3):
                for i in range(num_2,num_3-1,-1):
                    print(i)
            elif(num_2<num_3):
                for i in range(num_2,num_3+1):
                    print(i)
        elif(num_1<num_2):

            for i in range(num_1,num_2):
        
                print(i)
            if(num_2>num_3):
                for i in range(num_2,num_3-1,-1):

                    print(i)
            elif(num_2<num_3):
                for i in range(num_2,num_3+1): 

                    print(i)


if __name__=='__main__':
    run()


