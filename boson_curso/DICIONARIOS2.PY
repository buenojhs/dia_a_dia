elemento = {
    'z': 3,
    'nome': 'Lítio', 
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento["nome"]}')
print(f'Densidade: {elemento["densidade"]}')
print(f'O dicionario possui {len(elemento)} elementos.')


#atualizar uma entrada
elemento['grupo'] = 'Alcalinos'
print(elemento)

#adicionar uma entrada
elemento['periodo'] = 1
print(elemento)

#transforma em tuplas
print(elemento.items())
for i in elemento.items():
    print(i)
#acessar chaves
print(elemento.keys())
for i in elemento.keys():
    print(i)
#acessar valores
print(elemento.values())
for i in elemento.values():
    print(i)
#forma de tabela
for i, j in elemento.items():
    print(f'{i}:  {j}')