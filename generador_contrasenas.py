import random
def generador_contrasena():
    letras_m=['a','b','c','d','e','f','g','h','i']
    letras_M=['A','B','C','D','E','F','G','H','I']
    numeros=['1','2','3','4','5','6','7','8','9']
    simbolos = ['!','"','#','$','%','&','/','(',')','=']
    
    caracteres=letras_M+letras_m+numeros+simbolos

    contrasena=[]
    limite=int(input("contraseñas de cuantos digitos desea? "))
    for i in range(limite):
        caracteres_ale=random.choice(caracteres)
        contrasena.append(caracteres_ale)
    
    contrasena="".join(contrasena)
    return contrasena

def run():
    a="""DESEA GENERAR UNA CONTRASENA ALEATORIA?
        1.-SI
        2.-NO\n"""

    pregunta=input(a)
    if(pregunta=='1'):
        contrasena=generador_contrasena()
        print("su contrasena aleatoria es: "+contrasena)
    
    else:
        print("ok usted genere su propia contrasena:V")
    


if __name__=='__main__':
    run()