astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}
print(astros1 == astros2) #verifica se são iguais
print(astros1 != astros2) #verifica se são diferentes
print(astros1 | astros2)  #união dos conjuntos
print(astros1.union(astros2))  #união dos conjuntos

#intersecção dos conjuntos
print(astros1 & astros2)  #intersecção dos conjuntos
print(astros1.intersection(astros2))  #intersecção dos conjuntos

#diferença simétrica
print(astros1 ^ astros2)  #diferença simétrica dos conjuntos
print(astros1.symmetric_difference(astros2))  #diferença simétrica dos conjuntos


astros1.add('Urano')  #adiciona um elemento ao conjunto
astros1.add('Sol')
astros1.remove('Vênus')  #remove um elemento do conjunto
astros1.discard('XKD')
astros1.pop()  #remove um elemento aleatório do conjunto
astros1.clear()  #limpa o conjunto
print(astros1)
