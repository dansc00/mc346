import time

def warning(f):

    counter = 0 # marca a contagem de chamadas para envio do aviso
    startTime = 0 # marca tempo logo após a ocorrência de um aviso
    timer = 300 # tempo de intervalo entre avisos. 300 s = 5 min
    
    # decorator
    def wrapper(*args):

        nonlocal counter
        nonlocal startTime
        nonlocal timer

        # se o número de argumentos passado para a função é maior que 3
        if len(args) > 3:
            currentTime = time.time() # marca tempo atual

            # se ocorreram 10 chamadas após um aviso e o tempo de envio excedeu o intervalo de 5 min
            if counter == 0 and (currentTime - startTime) >= timer:
                # primeira iteração
                if(startTime == 0):
                    print(f"Tempo passado desde o último aviso: {0:.2f} minutos")
                else:
                    print(f"Tempo passado desde o último aviso: {(currentTime - startTime)/60:.2f} minutos")

                print("AVISO! - A função sumSquares será modificada na próxima implementação para aceitar apenas três argumentos")
                counter = 9 # reseta contador de chamadas
                startTime = currentTime # marca novo tempo logo após um aviso
            else:
                counter -= 1 # decrementa contador de chamadas

        res = f(*args) # chama função f
        
        return res

    return wrapper

@warning # sumSquares = warning(sumSquares)
# retorna soma dos produtos
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