# calculadora de risco de diabetes mellitus tipo 2

def calcular_risco_dm2():
    nome = input('Digite o seu nome para começar: ')
    print(f'Olá {nome}! Esse é um programa que avalia o risco de um indivíduo desenvolver Diabetes tipo 2. \n'
          'O valor do risco é baseados em estudos sobre o estilo de vida, histórico familiar e sua relação com a doença.\n'
          'Para isso, é necessário responder algumas questões sobre o seu estilo de vida e histórico familiar. Vamos começar!')
    
    pontuacao = 0
    risco_classificado = ''
    
    idade = int(input('Qual a sua idade?'))
    risco_idade = {
        (45, 54): 2,
        (54, 64): 3,
        (64, 110): 4,
    }
    
    for intervalo, risco in risco_idade.items():
        if intervalo[0] <= idade < intervalo[1]:
            pontuacao += risco
            break
    
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
    
    sexo = input('Qual o seu sexo? Digite F para feminino e M para masculino').strip().upper()     
    circunferencia_adbome = int(input('Qual sua circunferência abdominal medida abaixo da costela?'))
    
    if sexo == 'M':
      if 94 <= circunferencia_adbome < 102:
        pontuacao += 3
      elif circunferencia_adbome >= 102:
        pontuacao += 4
    elif sexo == 'F':
       if 80 <= circunferencia_adbome < 88:
         pontuacao += 3
       elif circunferencia_adbome >= 88:
        pontuacao += 4
    
    exercicio_fisico = input('Você faz ao menos 30 minutos de exercícios físicos no trabalho e/ou em seu tempo livre? Responda com SIM ou NÃO')
    if exercicio_fisico == 'não':
        pontuacao += 2

    alimentacao = input('Você come legumes, frutas ou sementes com frequência? Responda com SIM ou NÃO')
    if alimentacao == 'não':
        pontuacao += 1
    
    medicamento = input('Já fez uso de medicamento para pressão alta? Responda com SIM ou NÃO')
    if medicamento == 'sim':
        pontuacao += 2
    
    hiperglicemia = input('Já teve hiperglicemia? Responda com SIM ou NÃO')
    if hiperglicemia == 'sim':
        pontuacao += 2
        
    historico_familiar = input('Possui familiar próximo que já foi diagnosticado com diabetes?')
    if historico_familiar == 'sim':
        grau_familiar = input('Qual o grau de parentesco? Digite 1 para AVÓS, TIOS OU PRIMOS DE PRIMEIRO GRAU e 2 para PAIS,IRMÃOS OU FILHOS')

        risco_historico_f = {
         "1": 3,
         "2": 5
        }
        
        pontuacao += risco_historico_f.get(grau_familiar, 0)
        
    classificacao_de_risco = {
            (0, 7):'baixo',
            (7, 11):'um pouco elevado',
            (12, 14):'moderado',
            (15, 20):'alto,',
            (20, 23):'muito alto'
        }
        
    for intervalo, risco in classificacao_de_risco.items():
            if intervalo[0] <= pontuacao <= intervalo[1]:
                risco_classificado = risco
                break
                
    
    print(f"\n{nome}, sua pontuação de risco é: {pontuacao}.\n"
          f"Seu risco de desenvolver diabetes mellitus tipo 2 é {risco_classificado}.")