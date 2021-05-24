def palindromo(a):
    a=a.replace(' ','')
    a=a.lower()
    palabra_invertida=a[::-1]
    if a==palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("ingrese una palabra: \n")
    p_palindromo= palindromo(palabra)

    if(p_palindromo):
        print("es palidromo")
    else:
        print("no es palindromo")

if __name__=='__main__':
    run()