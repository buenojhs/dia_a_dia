produtos = 'carbonato de sódio e óxido de zinco'
print('sódio' in produtos)  # Verifica se 'sódio' está na string
print('magnésio' in produtos)  # Verifica se 'magnésio' está na string
print('magnésio' not in produtos)  # Verifica se 'magnésio' não está na string

item = 'hipoclorito'
pos = item.find('clor')  # Encontra a posição de 'clor' na string
print(pos)  # Exibe a posição encontrada
pos = item.find('flu')  # Tenta encontrar 'flu' na string
print(pos)  # Exibe -1 se não encontrado

objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste)
print(objeto_celeste.upper())  # Converte para maiúsculas
print(objeto_celeste.lower())  # Converte para minúsculas
print(objeto_celeste.title())  # Converte a primeira letra de cada palavra para
print(objeto_celeste.capitalize())  # Converte a primeira letra da string para maiúscula

suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio', 'zinco')  # Substitui valor na string
print(n_suplemento) #util para substituir palavras ou partes de strings ou textos

frase = '      Ômega 3 é bom para saúde!    '
print(frase)
print(frase.lstrip())  # Remove espaços à esquerda
print(frase.rstrip())  # Remove espaços à direita
print(frase.strip())  # Remove espaços à esquerda e à direita

fruta = 'abacate'
print(fruta)
print(fruta.rjust(20)) # Alinha à direita com 20 caracteres
print(fruta.center(20)) # Centraliza com 20 caracteres
print(fruta.ljust(20)) # Alinha à esquerda com 20 caracteres
print(fruta.ljust(20,  "-")) # Alinha à esquerda com 20 caracteres e preenche com '-'
print(fruta.center(20, "-")) # Centraliza com 20 caracteres e preenche

p = 'Bóson treinamentos'
print(p.startswith('Bó')) # Verifica se começa com 'Bó'
print(p.endswith('mentos')) # Verifica se termina com 'mentos'

#docstrings
""""
docstring é uma especie de documentacao
que podemos inserir dentro de um modulo, funcao
ou classe no python, entre outros locais
    respeita deslocamento do texto e é multilinhas
"""

#posso atribuir a ele uma variavel como = texto e depois chamar print



