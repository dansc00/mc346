-- Programa que imprima a soma dos elementos de uma lista

listSum [] = 0
listSum (x:xs) = x + listSum xs

main = do
    let list = [10,20,4,5,1]
    let listSum = listSum list
    print listSum
