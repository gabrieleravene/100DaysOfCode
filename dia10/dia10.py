# calculadora de dm2 aprimorada com tratamento de erros

def calcular_dm2():
    print('Calculadora de risco de Diabetes mellitus tipo 2.')
    nome = input('Digite o seu nome para começar: ')
    print(f'Olá, {nome}! Esse é um programa que avalia o risco de um indíviduo desenvolver Diabetes mellitus tipo 2.'
    'O valor do risco é baseado em estudos sobre o estilo de vida, histórico familiar e sua relação com a doença.'
    'Para isso, é necessário responder algumas questões sobre o estilo de vida e histórico familiar.')
    
    pontuacao = 0
    risco_classificado = ''
    
    while True:
        try:
              idade = int(input('Para começarmos, qual a sua idade?'))
              break
        except ValueError:
              print('Valor inválido. Tente novamente.')
           
    risco_idade = {
        (0, 45): 0,
        (45, 54): 2,
        (54, 64): 3,
        (64, 110): 4
    }
    
    for intervalo, risco in risco_idade.items():
       if intervalo[0] <= idade < intervalo[1]:
           pontuacao += risco
           break
       
    while True:
        try:   
            peso = float(input('Qual seu peso? '))
            altura = float(input('Qual sua altura?'))
            break
        except ValueError:
            print('Valor inválido. Tente novamente.')
        
    imc = peso / (altura ** 2)
    
    risco_imc = {
        (25,30): 1,
        (30, 100): 3,
    }
    
    for intervalo, risco in risco_imc.items():
        if intervalo[0] <= imc < intervalo[1]:
            pontuacao += risco
            break
    
    while True:
        try:
           circ = int(input('Digite sua circunferência abdominal: '))
           break
        except ValueError:
           print('Valor inválido. Tente novamente.')
           
    while True:
        sexo = input('Qual seu sexo? Insira M para masculino e F para feminino').strip().lower()
        if sexo not in['m', 'f']:
            print('Valor inválido. Tente novamente.')
        else:
            break
        
    if sexo == 'm':
        if 94 <= circ < 102:
            pontuacao += 3
        elif circ > 102:
            pontuacao += 4
    
    else:
        if 80 <= circ < 88:
            pontuacao += 3
        elif circ > 88:
            pontuacao += 4
        
    
    while True:
        exercicio_fisico = input('Você faz ao menos 30 minutos de exercícios físicos no trabalho e/ou em seu tempo livre (incluindo atividades normais diárias)? Responda com SIM ou NÃO').strip().lower()
        if exercicio_fisico not in ['sim', 'não']:
            print('Valor inválido. Tente novamente.')
        else:
            break
        
    if exercicio_fisico == 'não':
        pontuacao += 2
        
    while True:
        alimentacao = input('Você come legumes, frutas ou sementes com frequência? Responda com SIM ou NÃO').strip().lower()
        if alimentacao not in ['sim', 'não']:
            print('Valor inválido. Tente novamente.')
        else:
            break
        
    if alimentacao == 'não':
        pontuacao += 1
        
    
    while True:
        has = input('Você já tomou regularmente algum medicamento para pressão alta? Responda com SIM ou NÃO').strip().lower()
        if has not in ['sim', 'não']:
            print('Valor inválido. Tente novamente.')
        else:
            break
        
    if has == 'sim':
        pontuacao += 2
        
    while True:
        hiperglicemia = input('A sua taxa de glicose no sangue já foi alguma vez considerada alta? Responda com SIM ou NÃO').strip().lower()
        if hiperglicemia not in ['sim', 'não']:
            print('Valor inválido. Tente novamente.')
        else:
            break
        
    if hiperglicemia == 'sim':
        pontuacao += 2
        
    while True:
        familia = input('Algum membro da sua família ou parente próximo já foi diagnosticado com diabetes (tipo 1 ou tipo 2)? Responda com SIM ou NÃO').strip().lower()
        if familia not in ['sim', 'não']:
            print('Valor inválido. Tente novamente.')
        else:
            break
         
    if familia == 'sim':
        while True:
           try:
              grau = int(input('Digite 1 para avós, tios ou primos de primeiro grau e 2 para pais, filhos ou irmãos.'))
              if grau not in [1, 2]:
                  print('Digite 1 ou 2.')
              else:
                  break
           except ValueError:
            print('Digite um valor númerico.')
    
    if grau == 1:
            pontuacao +=3
    elif grau == 2:
            pontuacao += 5

    
    classificacao_risco = {
        (0, 7): 'baixo',
        (7, 11): 'um pouco elevado',
        (12, 14): 'moderado',
        (15, 20): 'alto',
        (20, 23): 'muito alto'
    }
    
    for intervalo, risco in classificacao_risco.items():
        if intervalo[0] <= pontuacao < intervalo[1]:
            risco_classificado = risco
            break
        
    print(f'\n{nome}, sua pontução é {pontuacao}')
    print(f'Isso significa que você possui um risco {risco_classificado} de desenvolver Diabetes tipo 2.')