def calcular_ganho_mensal():
    while True:
        try:
            ganho_por_dia_cheio = float(input('Qual o seu ganho por dia cheio?'))
            dia_cheio = float(input('Agora digite o número de dias cheios trabalhados'))
            if ganho_por_dia_cheio < 0:
                print('O ganho por dia livre não pode ser negativo. Insira um novo valor')
            elif dia_cheio >31:
                print('Existe tudo isso de dias no mês?!')    
            elif ganho_por_dia_cheio >= 500:
                print('Vamos falar sério né? Coloque um valor factível')    
            else:
                break
        except ValueError:
            print('Caracter Inválido. Utilize um valor (ex. 75.50) para o ganho nesse dia')
    while True:
        try:
            ganho_por_meios_dias = float(input('Qual o seu ganho por meio dia de trabalho?'))
            meios_dias = int(input('Agora digite o número de meios-dias trabalhados'))
            if meios_dias < 0:
                print('O numero de dias não pode ser negativo! Insira um valor positivo!')
            elif meios_dias >= 31:
                print('Existe tudo isso de dias no mês?!')
            elif ganho_por_meios_dias >=300:
                print('Vamos falar sério né? Coloque um valor factível')
            else:
                break
        except ValueError:
            print('Caracter Inválido. Utilize um valor (ex. 75.50) para o ganho nesse dia')

    #calculos
    total_dias = meios_dias + dia_cheio
    ganho_total_dias_cheios = dia_cheio * ganho_por_dia_cheio
    ganho_total_por_meios_dias = ganho_por_meios_dias * meios_dias
    ganho_total_mensal = ganho_total_dias_cheios + ganho_total_por_meios_dias
    return ganho_total_mensal

print(calcular_ganho_mensal())




