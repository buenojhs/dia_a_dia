#primeiro deve-se atribuir a lista de todos os parametros que sao obrigatorios e depois passar o valor para ele.
#depois da lista de obrigatorios eu posso passar os valores opcionais


def contar(num=11, caractere='+'):
    for i in range(1, num):
        print(caractere)

if __name__== '__main__':
    contar(caractere='&') #mostra na tela o caractere especificado
    contar(num=5) #mostra na tela o caractere o numero determinado de vezes
    contar(num=8, caractere='@') #mostra na tela o numero especificado de vezes o caractere especificado
    contar(6, '@') #faz a mesma coisa que o anterior



