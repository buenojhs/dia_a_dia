# lista representa uma sequencia de valores.

#sintaxe: nome_lista = [valores]

#notas = [5, 7, 8, 6, 9]
#print(notas)

n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 11]
valores = n1 + n2
#valores [0] = 9
#print(len(valores))
#print(sorted(valores))
#print(sorted(valores, reverse=True))
#print(sum(valores))
#print(max(valores))
#print(min(valores))

#valores.append(13)
#print(valores)
#valores.pop() #para eliminar um elemento especifico basta colocar a posicao
#print(valores)
#valores.insert(3, 21) #para inserir um elemento em uma posicao especifica
#print(valores)
#print(12 in valores) #para verificar se um valor esta na lista

planetas = ['Mercurio', 'Venus', 'Terra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:
    print(planeta)


