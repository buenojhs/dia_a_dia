#conjuntos coleções não ordenadas de valores únicos
#sets tem só valores, dicionarios tem valores e associam chaves
planeta_anao = {'PLutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)
#quantidade de elementos
print(len(planeta_anao))
#verifica se o elemento está no conjunto
print('Ceres'in planeta_anao)
#verifica se não esta em um conjunto
print('Terra' not in planeta_anao)

for astro in planeta_anao:
    print(astro)
    print(astro.upper()) #converte para maiusculo
    print(astro.lower()) #converte para minusculo
    print(astro.title()) #primeira letra maiuscula

astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print(astros, end=' ')
astro_set = set(astros)  #converte lista em conjunto, e valores iguais  eles não se repetem em um conjunto
print(astro_set)

