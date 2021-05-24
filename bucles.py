def run():
    LIMITE=1000
    contador=0
    num=2**contador
    while(num<LIMITE):
        print("el numero 2 elevado ",contador," es= ",num)
        contador+=1
        num=2**contador
if __name__=='__main__':
    run()