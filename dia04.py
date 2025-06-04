# sistema de cadastro de exames

import sqlite3

def criar_banco_de_dados():
    try:
        with sqlite3.connect("exames.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS exames (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nome_paciente TEXT,
                nome_exame TEXT,
                data_exame TEXT) """)
        
    except sqlite3.Error as erro:
        print(f'Erro ao banco de dados: {erro}.')
        
def cadastrar_exames():
    try:
        with sqlite3.connect("exames.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                paciente = input('Digite o nome do paciente que deseja cadastrar exame: ')
                exame = input('Digite o nome do exame: ')
                data = input('Digite a data do exame: ')
                
                cursor.execute(""" INSERT INTO exames (nome_paciente, nome_exame, data_exame)  values (?, ?, ?) """, (paciente, exame, data))
                
                conexao.commit()
                
                print('O exame foi cadastrado com sucesso.')
                
                continuar = input('Deseja continuar? (s/n)').strip().lower()
                if continuar != 's':
                    return
        
    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar exame: {erro}.')
        
def buscar_exames():
    try:
        with sqlite3.connect("exames.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                exame_procurado = input('Digite o ID do exame que deseja visualizar: ')
                
                cursor.execute(""" SELECT * FROM exames WHERE id = ? """, (exame_procurado,))
                exame = cursor.fetchone()
                
                if exame:
                    print("\nExame:")
                    print(f"ID do exame: {exame[0]} ")
                    print(f"Nome do paciente: {exame[1]}")
                    print(f"Nome do exame: {exame[2]}")
                    print(f"Data do exame: {exame[3]}")
                else:
                    print('Exame não consta no banco de dados.')
                    
        
    except sqlite3.Error as erro:
        print(f'Erro ao buscar exame em banco de dados: {erro}.')
        
def atualizar_exame():
    try:
        with sqlite3.connect("exames.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                    alteracao = input('Digite o ID do exame que deseja alterar:')
                    
                    cursor.execute(""" SELECT * FROM exames WHERE id =  ? """, (alteracao,))
                    
                    exame_procurado = cursor.fetchone()
                    
                    if exame_procurado:
                        print("\nExame:")
                        print(f"ID do exame: {exame_procurado[0]} ")
                        print(f"Nome do paciente: {exame_procurado[1]}")
                        print(f"Nome do exame: {exame_procurado[2]}")
                        
                        alterar = input('Digite o que deseja alterar (exame/data): ')
                        
                        if alterar == 'exame':
                            novo_exame = input('Digite a alteração a  ser feita: ')
                            
                            cursor.execute(""" UPDATE exames SET nome_exame = ? WHERE id = ? """, (novo_exame, alteracao))
                            
                            conexao.commit()
                            
                            print('Exame alterado com sucesso.')
                        
                        elif alterar == 'data':
                            nova_data = input('Digite a alteração a ser feita: ')
                            
                            cursor.execute(""" UPDATE exames SET data_exame = ? WHERE id = ? """, (nova_data, alteracao))
                            
                            conexao.commit()
                            
                            print('Exame alterado com sucesso.')
                            
                        else:
                            print('Opção inválida.')
                    
                    else: 
                        print('Exame não encontrado.')
                        
                    continuar = input('Deseja alterar mais exames? (s/n)')
                    if continuar != 's':
                       break
                                     
        
    except sqlite3.Error as erro:
        print(f'Erro ao atualizar exame: {erro}.')