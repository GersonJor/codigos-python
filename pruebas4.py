def recursiva(n):#recursiva sin return
    if(n<=1):
        print('+')
    else:
        recursiva(n-1)
        print(n)
        print(n*'+')
        

def run():
    recursiva(5)

if __name__=='__main__':
    run()