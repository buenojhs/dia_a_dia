#o comportamento da funcao muda conforme o numero de argumentos passados
#assim a funcao pode receber numeros diferentes de argumentos e ter comportamento diferente de acordo com o numero de argumentos passados



x = 5
y = 6
z = 3


def soma_mult(a,b,c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c
    
if __name__ == '__main__':
    res = soma_mult(x, y)
    print(res)

if __name__ == '__main__':
    res = soma_mult(x, y, z)
    print(res)