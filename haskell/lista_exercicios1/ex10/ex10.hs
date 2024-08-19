-- Programa que intercala 2 listas, sem exibir o restante. Ex: [1,2,6,7] e [3,5,8] = [1,3,2,5,6,8]

len [] = 0
len (l:ls) = len ls + 1

interX (x:xs) (y:ys) aux =
    interY xs 

inter [] [] aux = []
inter xs ys aux =
    if ((len xs) `mod` 2) == 0
    then interX xs ys aux
    else inter xs ys 


main = 
    do
    let list1 = [1,2,6,7]
    let list2 = [3,5,8]
    let aux = []
    let res = inter list1 list2 aux
    print res
