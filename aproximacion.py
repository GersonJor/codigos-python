# aproximacion con raices
objetivo=int(input("INGRESE UN NUMERO: "))
epsilon=0.01
paso=epsilon**2
respuesta=0.0

while abs(respuesta**2 - objetivo)>= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo),respuesta)
    respuesta+=paso

if(abs(respuesta**2 - objetivo)>= epsilon):
    print(f'NO SE ENCONTRO LA RAIZ CUADRADA {objetivo}')
else:
    print(f'la raiz cuadrada de {objetivo} es {respuesta}')