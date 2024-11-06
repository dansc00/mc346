# dado z um array 1D. Qual o valor em z com o maior valor absoluto? 
# Se z = np.array([4,-5,2]), 4 é o maior valor, mas -5 é o dado com maior valor absoluto. 
# A resposta deve ser -5 e nao 5 (eu nao quero o maior valor absoluto, eu quero o valor no array que tem o maior valor absoluto)

import numpy as np

z = np.array([1,2,-1,3,4,-6,5,-7,-8])
maxAbsPos = np.argmax(abs(z))

print(z[maxAbsPos])