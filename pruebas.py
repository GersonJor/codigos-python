# a=input("ingrese su nombre")
# b=input("ingrese su nombre")
# edad_1=int(input("hola "+a+" ingrese su edad"))
# edad_2=int(input("hola "+b+" ingrese su edad"))
# if(edad_1>edad_2):
#     print("el usuario llamado: "+a+" es mayor que "+b)
# elif(edad_1<edad_2):
#     print("el usuario llamado: "+b+" es mayor que "+a)
# else:
#     print(a+" y "+b+" tienen la misma edad")
contador_interno=1
contador_externo=1

while(contador_externo<5):
    while(contador_interno<6):
        print(contador_externo,contador_interno)
        contador_interno+=1
        

    contador_externo +=1
    contador_interno=1