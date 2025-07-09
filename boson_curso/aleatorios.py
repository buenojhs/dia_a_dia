import random

#valor = random.randint(1, 50)
#print(valor)

#print('gerar cinco numeros aleatorios entre 1 e 50: \n')
#for i in range(5):
#    n = random.randint(1, 50)
#    print(f'numero gerado: {n}')

#valor = random.random()
#print(f'numero gerado: {round(valor *10, 2)}')

#valor = random.uniform(1, 100)
#print(f'numero: {round(valor, 4)}')

#sortear valor dentro de uma lista

L = [ 2, 4, 6, 9, 10, 13, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
#n = random.choice(L)
#print(f'numero sorteado: {n}')

#n = random.sample(L, 3)
#print(f'valores sorteados: {n}')

#embaralhar

print(f'lista original: {L}')
print(f'embaralhar lista e exibi-la: ')
n = random.shuffle(L)
print(L)
