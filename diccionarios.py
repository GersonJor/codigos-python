poblacion_paises ={
    "ARGENTINA": 200_003_922,
    'PERU': 43_030_403,
    'MEXICO':50043453

}

# print(poblacion_paises['ARGENTINA'])
for i in poblacion_paises.keys():
    print(i)
for i in poblacion_paises.values():
    print(i)

for paises,poblacion in poblacion_paises.items():
    print("el pais "+paises+" tiene una poblacion de: ",poblacion)