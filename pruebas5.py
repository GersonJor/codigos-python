def fun(n):
    return lambda a:a*n

def run():
        dobler=fun(2)

        print(dobler(11))

if __name__=='__main__':
    run()