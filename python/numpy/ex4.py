# dado z um array 1D. substitua por 0 todos os elementos negativos de z

import numpy as np

z = np.array([1,2,-1,3,4,5,-6,-7,-8])

z = np.where(z >= 0, z, 0)

print(z)