# exceção é um objeto que representa um erro durante a execucao durante o programa
# blocos try... except

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

try: 
    r = round(n1 / n2, 2)    
except ZeroDivisionError: #se eu não excrever a excecao o programa nao trava, mas tb nao mostra o motivo do err0
    print(f'Não é possível dividir por zero!')
else:    
    print(f'Resultado: {r}')
#no try vai o codigo que eu suspeito que pode haver erro
#no except eu trato o erro
#else eu coloco o codigo que vai ser executado, é opcional

