# programa que avalia risco cardiovascular baseado no escore de framingham (risco de infarto ou morte por doença coronariana)

def calcular_riscocv():
    print('Avaliação de risco cardiovascular.')
    nome = input('Qual seu nome? ')
    
    print(f'Olá, {nome}.')
    
    while True:
        sexo = input('Qual seu sexo? (m/f)').strip().lower()
        if sexo not in ['m', 'f']:
            print('Valor inválido.')
        else:
            break
        
    if sexo == 'm':
        calcular_riscocv_m()
    else:
        calcular_riscocv_f()
        
def calcular_riscocv_f():
    pontuacao = 0
    risco_abs = ''
    
    while True:
        try:    
            idade = int(input('Qual sua idade? '))
            break
        except ValueError:
            print('Valor inválido.')
    
    risco_idade = {
        (20, 24): -7,
        (35, 39): -3,
        (40, 44): 0,
        (45, 49): 3,
        (50, 54): 6,
        (55, 59): 8,
        (60, 64): 10,
        (65, 69): 12,
        (70, 74): 14,
        (75, 79): 16
        }
        
    for intervalo, risco in risco_idade.items():
        if intervalo[0] <= idade < intervalo[1]:
            pontuacao += risco
            break
        
    while True:
        try:
            col = int(input('Qual seu nível de colesterol?'))
            break
        except ValueError:
            print('Valor inválido.')
            
    if 160 <= col < 199:
        if 20 <= idade < 39:
            pontuacao += 4
        elif 40 <= idade < 49:
            pontuacao += 3
        elif 50 <= idade < 59:
            pontuacao += 2
        elif 60 <= idade < 69:
            pontuacao += 1
        elif 70 <= idade < 79:
            pontuacao += 1
            
    if 200 <= col < 239:
        if 20 <= idade < 39:
           pontuacao += 8
        elif 40 <= idade < 49:
            pontuacao += 6
        elif 50 <= idade < 59:
            pontuacao += 4
        elif 60 <= idade < 69:
            pontuacao += 2
        elif 70 <= idade < 79:
            pontuacao += 1
            
    if 240 <= col < 279:
        if 20 <= idade < 39:
           pontuacao += 11
        elif 40 <= idade < 49:
            pontuacao += 8
        elif 50 <= idade < 59:
            pontuacao += 5
        elif 60 <= idade < 69:
            pontuacao += 3
        elif 70 <= idade < 79:
            pontuacao += 2
            
    if col >= 280:
        if 20 <= idade < 39:
           pontuacao += 13
        elif 40 <= idade < 49:
            pontuacao +=10
        elif 50 <= idade < 59:
            pontuacao += 7
        elif 60 <= idade < 69:
            pontuacao += 4
        elif 70 <= idade < 79:
            pontuacao += 2
    
    while True:        
        fumo = input('Você fuma? (s/n)').strip().lower()
        if fumo not in ['s', 'n']:
            print('Valor inválido.')
        else:
            break
        
    if fumo == 's':
        if 20 <= idade < 39:
            pontuacao += 9
        elif 40 <= idade < 49:
            pontuacao += 7
        elif 50 <= idade < 59:
            pontuacao += 4
        elif 60 <= idade < 69:
            pontuacao += 2    
        elif 70 <= idade < 79:
            pontuacao += 1
        
    while True:
        try:
            hdl = int(input('Qual seu nível de HDL?'))
            break
        except ValueError:
            print('Valor inválido.')
            
    if hdl >= 60:
        pontuacao -= 1
    elif 40 <= hdl < 49:
        pontuacao += 1
    elif hdl < 40:
        pontuacao += 2
    
    while True:
        try:
            pa = int(input('Qual sua PA? (sistólica mm Hg)'))
            break
        except ValueError:
            print('Valor inválido.')
            
    if pa > 120:
        while True:
            tratamento = input('Tratada? (s/n)').strip().lower()
            if tratamento not in ['s', 'n']:
                print('Valor inválido.')
            else:
                break
            
        if tratamento == 's':
            if 120 <= pa < 129:
                pontuacao += 3
            elif 130 <= pa < 139:
                pontuacao += 4
            elif 140 <= pa < 159:
                pontuacao += 5
            elif pa >= 160:
                pontuacao += 6
        
        elif tratamento == 'n':
            if 120 <= pa < 129:
                pontuacao += 1
            elif 130 <= pa < 139:
                pontuacao += 2
            elif 140 <= pa < 159:
                pontuacao += 3
            elif pa >= 160:
                pontuacao += 4
            
    risco_classificado = {
        (-50, 9): '< 1 %',
        (9, 13): '1 %',
        (13, 15): '2 %',
        (15, 16): '3 %',
        (16, 17): '4 %',
        (17, 18): '5 %',
        (18, 19): '6 %',
        (19, 20): '8 %',
        (20, 21): '11 %',
        (21, 22): '14 %',
        (22, 23): '17 %',
        (23, 24): '22 %',
        (24, 25): '27 %',
        (25, 50): '> 30 %',
    }
    
    for intervalo, risco in risco_classificado.items():
        if intervalo[0] <= pontuacao <= intervalo[1]:
            risco_abs = risco
            break
        
    print(f'Sua pontuação é {pontuacao}. \n')
    print(f'Seu risco cardiovascular é {risco_abs}.')
    

def calcular_riscocv_m():
    pontuacao = 0
    risco_abs = ''
    
    while True:
        try:    
            idade = int(input('Qual sua idade? '))
            break
        except ValueError:
            print('Valor inválido.')
    
    risco_idade = {
        (20, 34): -9,
        (35, 39): -4,
        (40, 44): 0,
        (45, 49): 3,
        (50, 54): 6,
        (55, 59): 8,
        (60, 64): 10,
        (65, 69): 11,
        (70, 74): 12,
        (75, 79): 13
    }
        
    for intervalo, risco in risco_idade.items():
        if intervalo[0] <= idade < intervalo[1]:
            pontuacao += risco
            break
        
            
    while True:
        try:
            col = int(input('Qual seu nível de colesterol?'))
            break
        except ValueError:
            print('Valor inválido.')
            
    if 160 <= col < 199:
        if 20 <= idade < 39:
            pontuacao += 4
        elif 40 <= idade < 49:
            pontuacao += 3
        elif 50 <= idade < 59:
            pontuacao += 2
        elif 60 <= idade < 69:
            pontuacao += 1
            
    if 200 <= col < 239:
        if 20 <= idade < 39:
           pontuacao += 4
        elif 40 <= idade < 49:
            pontuacao += 3
        elif 50 <= idade < 59:
            pontuacao += 2
        elif 60 <= idade < 69:
            pontuacao += 1
            
    if 240 <= col < 279:
        if 20 <= idade < 39:
           pontuacao += 9
        elif 40 <= idade < 49:
            pontuacao += 6
        elif 50 <= idade < 59:
            pontuacao += 4
        elif 60 <= idade < 69:
            pontuacao += 2
        elif 70 <= idade < 79:
            pontuacao += 1
            
    if col >= 280:
        if 20 <= idade < 39:
           pontuacao += 11
        elif 40 <= idade < 49:
            pontuacao += 8
        elif 50 <= idade < 59:
            pontuacao += 5
        elif 60 <= idade < 69:
            pontuacao += 3
        elif 70 <= idade < 79:
            pontuacao += 1
    
    while True:        
        fumo = input('Você fuma? (s/n)').strip().lower()
        if fumo not in ['s', 'n']:
            print('Valor inválido.')
        else:
            break
        
    if fumo == 's':
        if 20 <= idade < 39:
            pontuacao += 8
        elif 40 <= idade < 49:
            pontuacao += 5
        elif 50 <= idade < 59:
            pontuacao += 3
        elif 60 <= idade < 69 or 70 <= idade < 79:
            pontuacao += 1    
        
        
    while True:
        try:
            hdl = int(input('Qual seu nível de HDL?'))
            break
        except ValueError:
            print('Valor inválido.')
            
    if hdl >= 60:
        pontuacao -= 1
    elif 40 <= hdl < 49:
        pontuacao += 1
    elif hdl < 40:
        pontuacao += 2
    
    while True:
        try:
            pa = int(input('Qual sua PA? (sistólica mm Hg)'))
            break
        except ValueError:
            print('Valor inválido.')
            
    if pa > 120:
        while True:
            tratamento = input('Tratada? (s/n)').strip().lower()
            if tratamento not in ['s', 'n']:
                print('Valor inválido.')
            else:
                break
            
        if tratamento == 's':
            if 120 <= pa < 129:
                pontuacao += 1
            elif 130 <= pa < 139:
                pontuacao += 2
            elif 140 <= pa < 159:
                pontuacao += 2
            elif pa >= 160:
                pontuacao += 3
        
        elif tratamento == 'n':
            if 130 <= pa < 139:
                pontuacao += 1
            elif 140 <= pa < 159:
                pontuacao += 1
            elif pa >= 160:
                pontuacao += 2
            
    risco_classificado = {
        (-50, 1): '<1 %',
        (1, 5): '1 %',
        (5, 7): '2 %',
        (7, 8): '3 %',
        (8, 9): '4 %',
        (9, 10): '5 %',
        (10, 11): '6 %',
        (11, 12): '8 %',
        (12, 13): '10 %',
        (13, 14): '12 %',
        (14, 15): '16 %',
        (15, 16): '20 %',
        (16, 17): '25 %',
        (17, 50): '>30 %'
    }
    
    for intervalo, risco in risco_classificado.items():
        if intervalo[0] <= pontuacao <= intervalo[1]:
            risco_abs = risco
            break
        
    print(f'Sua pontuação é {pontuacao}. \n')
    print(f'Seu risco cardiovascular é {risco_abs}.')