# Funções
# criar um codigo modular, onde pode haver um reuso de código

#def <nome_funcao> ([argumentos]):
#    <instricoes>

#def mensagem():
#    print('Bóson Treinamentos em tecnologia')
#    print('Curso Completo de Python.')

#mensagem()

#funcao com argumentos

#def soma(a, b):
#    print(a+b)

#soma(12, 7)

#def multi(x, y):
#    return x * y

#a = 5
#b = 8
#c = multi(a, b)
#print(f'O produto de {a} e {b} é {c}')

def div(k, j):
    if j != 0:
        return k / j
    else:
        return 'Impossível dividir por zero!'

if __name__ == '__main__':
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = div(a, b)
    print(f'{a} dividido por {b} é igual a {r}')