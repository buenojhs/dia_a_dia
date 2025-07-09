#laço externo e laço interno
#encadeamento de laçoes de repetição
#for cont_ex in range(1, 3):
#    print(f'\nRodada: {cont_ex}')
    #laço interno, roda após cada rodada do laço externo
#    for cont_in in range(5, 0, -1):
#        print(f'Valor: {cont_in}')

#print( 'fim dos lacos')

import random

for A in range(1,6):
    print(f'\nConjunto {A}')
    for B in range(5):
        num = random.randint(1, 100)
        print(f'Valor: {num}')