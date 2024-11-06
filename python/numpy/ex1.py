#dado X um array 2D com 10 linhas. Some 10.0 aos elementos da 1a linha, 20.0 aos da 2a, 30.0 aos da terceira e assim por diante

import numpy as np

X = np.arange(30).reshape(10,3)

acc = 10
pos = 0
for row in X:
    X[pos] = row + acc
    acc += 10
    pos += 1

print(X)