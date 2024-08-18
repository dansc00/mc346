-- Recebe uma posição n e imprime a lista invertida de n até a posição 1

rangeRev _ _ [] = []
rangeRev count n [x:xs] = rangeRev count n xs 
    count = count + 1
    if count == n
    then print x
    else 