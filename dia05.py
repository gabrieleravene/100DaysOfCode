# sistema de cadastro de exames

import sqlite3

def criar_banco_de_dados():
    try:
        with sqlite3.connect("exameslab.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS exame (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_paciente TEXT,
                nome_exame TEXT,
                data_exame TEXT) """)   
    
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def cadastrar_exame():
    try:
        with sqlite3.connect("exameslab.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                paciente = input('Digite o nome do paciente que deseja cadastrar exame: ')
                exame = input('Digite o nome do exame: ')
                data = input('Digite a data do exame: ')
                    
                cursor.execute(" INSERT INTO exame (nome_paciente, nome_exame, data_exame) values (?, ?, ?) ", (paciente, exame, data,))
                    
                conexao.commit()
                    
                print('Exame cadastrado com sucesso.')
                    
                continuar = input('Deseja cadastrar mais exames? (s/n) ')
                if continuar != 's':
                    break

    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar exame no banco de dados: {erro}.')
        
def visualizar_exame():
    try:
        with sqlite3.connect("exameslab.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                paciente = input('Digite o paciente que deseja visualizar exame: ')
                
                cursor.execute("""SELECT * FROM exame WHERE nome_paciente = ?""", (paciente,))
                paciente_encontrado = cursor.fetchone()
                
                if paciente_encontrado:
                    print("\nExame:")
                    print(f"ID do exame: {paciente_encontrado[0]}")
                    print(f"Nome do paciente: {paciente_encontrado[1]}")
                    print(f"Nome do exame: {paciente_encontrado[2]}")
                    print(f"Data do exame: {paciente_encontrado[3]}")
                    
                else:
                    print('Paciente não encontrado.')
                    
                continuar = input('Deseja buscar mais exames? (s/n)')
                if continuar != 's':
                    break
        
    except sqlite3.Error as erro:
        print(f'Erro ao buscar exame no banco de dados: {erro}.')
    
def atualizar_exame():
    try:
        with sqlite3.connect("exameslab.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                paciente = input('Digite o nome do paciente que deseja alterar o exame: ')
                
                cursor.execute(""" SELECT * FROM exame WHERE nome_paciente = ? """, (paciente,))
                paciente_procurado = cursor.fetchone()
                
                if paciente_procurado:
                    print("\nPaciente encontrado:")
                    print(f"ID do exame: {paciente_procurado[0]}")
                    print(f"Nome do paciente: {paciente_procurado[1]}")
                    print(f"Nome do exame: {paciente_procurado[2]}")
                    print(f"Data do exame: {paciente_procurado[3]}")
                    
                    atualizar = input('Digite o que deseja alterar (exame/data): ')
                    if atualizar == 'exame':
                        alteracao = input('Digite alteracao a ser feita: ')
                        
                        cursor.execute(""" UPDATE exame SET nome_exame = ? WHERE nome_paciente = ? """, (alteracao, paciente))
                        
                        conexao.commit()
                        
                        print('Exame alterado com sucesso.')
                        
                        
                    elif atualizar == 'data':
                        alteracao = input('Digite a alteração a ser feita: ')
                        
                        cursor.execute(""" UPDATE exame SET data_exame = ? WHERE nome_paciente = ? """, (alteracao, paciente))
                        
                        conexao.commit()
                        
                        print('Data alterada com sucesso.')
                        
                    else:
                        print('Exame não encontrado.')
                        
                        
                    continuar = input('Deseja alterar mais exames? (s/n)')
                    if continuar != 's':
                        break
                    
                else:
                    print('Paciente não encontrado.')
        
    except sqlite3.Error as erro:
        print(f'Erro ao alterar exame.')
        

def deletar_exame():
    try:
        with sqlite3.connect("exameslab.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                exame_id = input('Digite o ID do exame que deseja eliminar: ')
                
                cursor.execute(""" SELECT * FROM exame WHERE id = ? """, (exame_id,))
                exame = cursor.fetchone()
                
                if exame:
                    print("\nExame:")
                    print(f"ID do exame: {exame[0]}")
                    print(f"Nome do paciente: {exame[1]}")
                    print(f"Nome do exame: {exame[2]}")
                    print(f"Data do exame: {exame[3]}")
                    
                    confirmacao = input('Deseja realmente deletar esse exame? (s/n)').strip().lower()
                    
                    if confirmacao == 's':
                        cursor.execute(""" DELETE FROM exame WHERE id = ? """, (exame_id,))
                        
                        conexao.commit()
                        
                        print('Exame eliminado com sucesso.')
                
                continuar = input('Deseja elimar mais exames? (s/n)')
                if continuar != 's':
                    break      
    
    except sqlite3.Error as erro:
        print(f'Erro ao deletar exame: {erro}.')