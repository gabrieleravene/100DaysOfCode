# calculadora de risco de diabetes mellitus tipo 2

def calcular_dm2():
    nome = input('Digite o seu nome para começar: ')
    print(f'\nOlá, {nome}! Esse é um programa que avalia o risco de um indíviduo desenvolver Diabetes mellitus tipo 2.'
    'O valor do risco é baseados em estudos sobre o estilo de vida, histórico familiar e sua relação com a doença.'
    'Para isso, é necessário responder algumas questões sobre o estilo de vida e histórico familiar.')
    
    pontuacao = 0
    risco_classificado = ''
    
    idade = int(input('Qual a sua idade?'))
    risco_idade = {
        (45, 54): 2, # chaves são tuplas que representam intervalo de idade (45-45)
        (54, 64): 3,
        (64, 110): 4,
    }
    
    for intervalo, risco in risco_idade.items():
        if intervalo[0] <= idade < intervalo[1]: # verifica se idade está dentro de intervalo específico
            pontuacao += risco
            break # interrompe o for assim que encontrar o primeiro intervalo correspondente
        
    peso = float(input('Qual o seu peso?'))
    
    altura = float(input('Qual a sua altura?'))
    
    imc = peso / (altura ** 2)
    
    risco_imc = {
        (25, 30): 1,
        (30, 100): 3
    }
        
    for intervalo, risco in risco_imc.items():
        if intervalo[0] <= imc < intervalo[1]:
            pontuacao += risco
            break
        
    sexo = input('Qual seu sexo? Digite M para masculino e F para feminino: ').strip().lower()
    circ = float(input('Digite sua circunferência abdominal: '))
    
    if sexo == 'M':
        if 94 <= circ < 102:
            pontuacao += 3
        elif circ >= 102:
            pontuacao += 4
    elif sexo == 'F':
        if 80 <= circ < 88:
            pontuacao += 3
        elif circ >= 88:
            pontuacao += 4
    
    exercicio_fisico = input('Você faz ao menos 30 minutos de exercícios físicos no trabalho e/ou em seu tempo livre? Responda com SIM ou NÃO.').strip().lower()
    if exercicio_fisico == 'não':
        pontuacao += 2
        
    alimentacao = input('Você come legumes, frutas ou sementes com frequência? Responda com SIM ou NÃO.').strip().lower()
    if alimentacao == 'não':
        pontuacao += 1
        
        
    medicamento = input('Já fez uso de medicamento para pressão alta? Responda com SIM ou NÃO').strip().lower()
    if medicamento == 'sim':
        pontuacao += 2
        
    hiperglicemia = input('Já teve hiperglicemia Responda com SIM ou NÃO').strip().lower()
    if hiperglicemia == 'sim':
        pontuacao += 2
        
    historico_familiar = input('Possui algum membro da família ou parente próximo diagnosticado com diabetes? Responda com SIM ou NÃO').strip().lower()
    if historico_familiar == 'sim':
        grau_f = input('Qual o grau de parenteresco? Digite 1 para avós, tios ou primos de primeiro grau OU 2 para pais, irmãos ou filhos')
        
        risco_hf = {
            "1": 3,
            "2": 5
        }
        
        pontuacao += risco_hf.get(grau_f, 0)

    risco_classificado = {
        (0, 7): 'baixo',
        (7, 11): 'um pouco elevado',
        (12, 14): 'moderado',
        (15, 20): 'alto',
        (20, 23): 'muito alto'
    }
    
    for intervalo, risco in risco_classificado.items():
        if intervalo[0] <= pontuacao <= intervalo[1]:
            risco_classificado = risco
        
    print(f'{nome}, Sua pontuação é {pontuacao}.'
    f'Isso significa que seu risco de desenvolver Diabetes tipo 2 é {risco_classificado}.')