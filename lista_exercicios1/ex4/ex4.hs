-- Programa que soma os valores pares em uma lista

isEven x = if x `mod` 2 == 0
    then True
    else False

evenSum [] = 0
evenSum (x:xs) = do
    let flag = isEven x
    let aux = 0
    if x == True
    then aux + evenSum xs
    else evenSum xs

main = do
    let list = [2,4,3,7,6]
    let res = evenSum list
    print res