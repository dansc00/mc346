import time

def warning(f):

    flag = 0
    startTime = 0
    endTime = 0
    timer = 300
 
    def wrapper(*args):

        nonlocal flag
        nonlocal startTime
        nonlocal endTime
        nonlocal timer

        if(len(args) > 3):

            if(flag <= 0 and startTime > 0):
                endTime = time.time()

            if(flag <= 0 and ((endTime - startTime) >= timer or (endTime - startTime == 0))):
                print(f"Tempo passado desde o último aviso: {(endTime - startTime)/60} minutos")
                print("AVISO! - A função sumSquares será modificada na próxima implementação para aceitar apenas três argumentos")
                flag = 10
                startTime = time.time()
            else:
                flag = flag - 1

        res = f(*args)
        
        return res

    return wrapper

@warning
def sumSquares(*args):

    res = 0
    for i in args:
        res += i**2

    return res
 
for i in  range(31):
    print(f"Iteração {i}")
    print(sumSquares(1,2,3,4))
    if i <= 12: 
        time.sleep(60)  #  1 minuto
    print(sumSquares(1,2,3))
    print("")



#for i in range(0, 32):
#    print(sumSquares(1,2,3,4))
#    time.sleep(1)

