# dado z um array 1D. Remova de z todos os elementos negativos (retorna um novo array)

import numpy as np

z = np.array([1,2,-1,3,4,5,-6,-7,-8])

z = z[z >= 0]

print(z)