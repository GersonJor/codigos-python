def metodo(mensaje,valor_dolar):
    valor=input("ingrese el numero de " +mensaje+ " que tiene: ")
    valor=float(valor)
    dolares=valor/valor_dolar
    dolares=round(dolares,2) 
    print("tienes $ ",dolares ," dolares")

menu="""
Bienvenido al conversor de monedas😁:)
  1.soles peruanos
  2.pesos argentinos
  3.pesos mexicanos
  
  Eliga una de las opciones: """
opcion =int( input(menu))



if opcion==1:
    metodo("soles peruanos",3,60)
elif opcion==2:
    metodo("pesos argentinos",65)
elif opcion==3:
    metodo("pesos mexicanos",24)
else:
      print("error, ingrese una opcion correcta.")
   
         


