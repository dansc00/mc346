# dado X um array 2D com 10 Colunas. Some 10.0 aos elementos da 1a coluna, 20.0 aos da 2a, 30.0 aos da terceira e assim por diante

import numpy as np

X = np.arange(30).reshape(3,10)

acc = 10
i = 0
j = 0

for row in X:
    for column in row:
        X[i][j] = column + acc
        j += 1
        acc += 10
    i += 1
    j = 0
    acc = 10 

print(X)