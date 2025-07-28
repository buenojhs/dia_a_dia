#funções lambda (anônimas)
#sintaxe:
# lambda argumentos: expressão

quadrado = lambda x: x**2

for i in range(1, 11):
    print(quadrado(i))
#abaixo como verificar se o número é par
par = lambda x: x %2 == 0
print(par(8))

#calcular celcius para F

f_c = lambda f: (f - 32) * 5/9
print(f_c(32))

# função map()
# sintaxe
# map(função, iterável)

#multiplicar valores de uma lista por 2

num = [1, 2, 3, 4, 5, 6, 7, 8]
dobro = list(map(lambda x: x*2, num))
print(dobro)

#converter tudo para caixa alta

palavras = ['python', 'é', 'uma', 'linguaguem', 'de', 'programação']
maiúsculas = list(map(str.upper, palavras))
print(maiúsculas)
print(palavras)