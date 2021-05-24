import random


def run():
    resp='si'
    while(resp!='no'):
    
        intentos=4
    
        nmr_aleatorio=random.randint(1,100)
        nmr_elegido=int(input("elige un numero del 1 al 100: \n"))
    
        while(nmr_elegido!=nmr_aleatorio ):
        
        
            if(nmr_elegido<1 or nmr_elegido>100):
               print("ERROOORR\n NUMERO INGRESADO NO ESTA EN EL RANGO DEL 1 AL 100")
               break
            else:
                 if(nmr_elegido<nmr_aleatorio):
                    print("\ningrese un numero mas mayor!")
                 else:
                    print("\ningrese un numero mas pequeño!")
            
                 nmr_elegido=int(input("\ningrese denuevo otro numero: "))
                 intentos-=1
                 print("te quedan ",intentos," intentos.")
                 if(intentos==0):
                    print("GAME OVERR :,(")
                    print("el numero aleatorio era: ",nmr_aleatorio)
                    break
           
        if(nmr_elegido==nmr_aleatorio):
           print("Felicidades ganaste te quedaron: ",intentos," intentos")
        else:
            print("error")
        print("desea continuar <si/no>")
        resp=input()
        
    
   
    
      


if __name__=='__main__':
    run()