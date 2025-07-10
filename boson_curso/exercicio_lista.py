# crie um script que peça para o usuario digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista.
# na sequencia, exiba na tela os elementos da lista em ordem alfabetica, um por linha, usando um laço de repeticao for

bebidas = []

for i in range(5):
    print(f'Digite uma bebida favorita: ')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()

print(f'\nBebidas Escolhidas: ')
for bebida in bebidas:
    print(bebida)

