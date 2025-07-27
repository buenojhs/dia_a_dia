#indica a visibillidade de uma variavel dentro do codigo
#pode ser global: criada fora das funcoes e pode ser acessada por todo o codigo onde for chamada
#pode ser local: criada dentro de uma funcao ou rotina existindo dentro dela
#preferir uso de variaveis locais

var_global = "Curso Completo de Python"

def escreve_texto():
    #global var_global #nesse caso altera o conteudo da variavel global de dentro de uma funcao
    var_global = "Bancos de Dados com SQL" #nesse caso ele altera a "variavel global" apenas dentro dessa funcao e nao a de fora(a global de fato)
    var_local = "Jorge Henrique"
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')
    