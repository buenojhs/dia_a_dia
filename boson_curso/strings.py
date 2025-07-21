nome = 'curso de python'
instrutor = 'jorge'
letra = nome[2]
print(letra)
print(len(nome))
print(nome + ' com ' + instrutor)

frase = 'vamos aprender python hoje. '
palavras = frase.split() #quebra a frase em palavras, lista de strings
print(palavras)
for palavra in palavras:
    print(palavra)

print(frase[0:5]) #fatiamento
print(frase[6:14])
print(frase[7:19])
print(frase[7:]) #do 7 até o final
print(frase[:5]) #do começo até o 5
print(frase[-5:]) #do -5 até o final

email = input('digite seu endereço de email: ')
arroba = email.find('@')
print(arroba)

usuario = email[0:arroba] #fatiamento do email
dominio = email[arroba+1:] #fatiamento do dominio
print(usuario)
print(dominio)
