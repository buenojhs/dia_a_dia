#função filter()
#sintaxe:
# filter(função, sequência)

def numeros_pares(n):
    return n % 2 == 0
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

num_par = list(filter(numeros_pares, numeros))
print(num_par)


numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
num_impar = list(filter(lambda x: x%2 != 0, numeros))
print(num_impar)

#função reduce()
#sintaxe
#reduce(função, sequência, valor_inicial)
#é uma função cumulativa

from functools import reduce

def mult(x, y):
    return x * y

numeros = [1,2,3,4,8,6]

total = reduce(mult, numeros)
print(total)

# soma cumulativa dos quadrados de valores, usando expressão lambda

numeross = [1,2,3,4]
# 1 ao quadrado + 2 ao quadrado + 3 ao quadrado + 4 ao quadrado

total = reduce(lambda x, y: x**2 + y**2, numeross)
print(total)
