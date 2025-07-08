# simples, composto, encadeado

#simples

n1 = n2 = 0.0

media = 0.0

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

#calcular media aritmetica
media = (n1 + n2) / 2

if (media >= 7):
    print("Aprovado")
    print("parabens")
elif (media >= 5):
    print("voce esta de recuperacao")    
else:
    print("Reprovado")
    print("Estude mais")    
print( 'sua media é {} '.format(media))



