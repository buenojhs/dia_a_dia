#lista = [1, 2, 3, 4, 5]
#palavra = 'boson'
#for letra in palavra:
#    print(letra)

#for numero in range(1, 11):
#    print(numero)

#nome = input('Digite seu nome: ')
#for x in range(10):
#    print(f'{x+1} {nome}')

# range (valor_inicial, valor_final, incremento)

#for x in range(2, 20, 3):
#    print(x)

pedras = ('rubi', 'esmeralda', 'diamante', 'safira', 'topázio', 'ágata')

for pedra in pedras:
    if pedra == 'safira':
        continue
    print(pedra)