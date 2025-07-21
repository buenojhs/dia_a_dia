def calcular_somas():
    valores_semana_livre = {
        'segunda_livre': 250,
        'terca_livre': 250,
        'quarta_livre': 250,
        'quinta_livre': 250,
        'sexta_livre': 250,
        
    }
    valores_semana_ocupado = {
        'segunda_livre': 250,
        'terca_ocupado': 200,
        'quarta_livre': 250,
        'quinta_livre': 250,
        'sexta_ocupado': 200,
    }

    soma_semana_livre = sum(valores_semana_livre.values())
    soma_semana_ocupado = sum(valores_semana_ocupado.values())
    return soma_semana_livre, soma_semana_ocupado

livre, ocupado = calcular_somas()
print(livre)
print(ocupado)

