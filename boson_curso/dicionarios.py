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

#exclusão de itens em dicionários
del elemento['periodo']
print(elemento)


#apagar tudo do dicionário
elemento.clear()
print(elemento)

