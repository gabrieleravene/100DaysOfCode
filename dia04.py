# sistema de cadastro de exames
# create, read, update

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
                    print('Exame encontrado.')
                    return {
                        "id":exame[0],
                        "nome_paciente":exame[1],
                        "nome_exame":exame[2],
                        "data_exame":exame[3]}
                else:
                    print('Exame não consta no banco de dados.')
                    
        
    except sqlite3.Error as erro:
        print(f'Erro ao buscar exame em banco de dados: {erro}.')
        
def atualizar_exame():
    try:
        with sqlite3.connect("exames.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                paciente = input('Digite o nome do paciente que deseja alterar o exame: ')
                
                cursor.execute(""" SELECT * FROM exames WHERE nome_paciente = ? """, (paciente,))
                paciente_procurado = cursor.fetchone()
                
                if paciente_procurado:
                    alteracao = input('Digite o ID do exame que deseja alterar:')
                    
                    cursor.execute(""" SELECT * FROM exames WHERE id =  ? """, (alteracao,))
                    
                    exame_procurado = cursor.fetchone()
                    
                    if exame_procurado:
                        alterar = input('Digite o que deseja alterar (exame/data): ')
                        
                        if alterar == 'exame':
                            novo_exame = input('Digite a alteração a  ser feita: ')
                            
                            cursor.execute(""" UPDATE exames SET nome_exame = ? WHERE id = ? """, novo_exame, alteracao, )
                            
                            conexao.commit()
                            
                            print('Exame atualizado com sucesso.')
                                     
        
    except sqlite3.Error as erro:
        print(f'Erro ao atualizar exame: {erro}.')
        
        