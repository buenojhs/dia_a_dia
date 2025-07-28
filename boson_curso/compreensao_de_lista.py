numeros = [1,4,7,9,10,12,21]
#usando a função map
quadrados = list(map(lambda num: num**2, numeros))
print(quadrados)

#usando compreensão de lista

quadrados = [num**2 for num in numeros]
print(quadrados)

# criando lista de numeros pares de 0 a 100

pares = [num for num in range(100) if num % 2 == 0]
print(pares)

# calcular vogais

frase = 'A lógica é apenas o princípio da sabedora, e não o seu fim'
vogais = ['a', 'e', 'i','o', 'u', 'á', 'é', 'í', 'ó', 'ú']

lista_vogais = [v for v in frase if v in vogais]
print(f'A frase possui {len(lista_vogais)} vogais: ')
print(lista_vogais)


# distributiva entre valores de duas listas
# se o código ficar muito extenso, melhor utilizar laço de repetição convencional
# como dois laços for encadeados

distributiva = [k * m for k in [2,3,5] for m in [10, 20, 30]]
print(distributiva)