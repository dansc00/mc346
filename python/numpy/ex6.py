# dado z um array 1D. Qual a posicao do maior valor em z

import numpy as np

z = np.array([1,2,-1,3,4,-6,5,-7,-8])

maxPos = np.argmax(z)
print(maxPos)