# são imutaveis

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn')
#concatenacao
elementos = halogenios + gases_nobres
t1 = (1, 5, 2, 6, 8, 4, 5, 6, 4, 4, 0, 12, 22, 3, 4, 5)
print(t1.count(3)) # contar quantas vezes o elemento aparece
print(elementos)
print(halogenios[0:2]) # fatiamento, comeca a contar do zero
print(halogenios[1:]) # do segundo elemento ate o final
print(halogenios[-3:]) # do terceiro elemento do final ate o final
print ('Fe' in halogenios) # verificar se o elemento esta na tupla
print(sum(t1)) # soma dos elementos
print(max(t1)) # maior elemento
print(min(t1)) # menor elemento

#operacoes nao disponiveis em tuplas: .sort(), .append(), .insert(), .remove(), .pop(), .reverse().pop()...

for elemento in elementos:
    print(f'Elemento: {elemento}')

grupo17 = list(halogenios) # converter tupla em lista
grupo12[0] = 'H'
print(grupo17)

#lista a partir de tuplas

alcalinos = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
grupo1 = tuple(alcalinos)  # converter lista em tupla
print(grupo1)

#comando type verifica o tipo de dado

print (sorted(alcalinos)) # ordena a lista
