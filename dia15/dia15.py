import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "listadetarefas.db")

def criar_banco_de_dados():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarefa TEXT,
                status TEXT) """)
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def criar_tarefa():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                tarefa = input('Digite a tarefa: ')
                status = input('Digite o status: ')
                
                cursor.execute(""" INSERT INTO tarefas (tarefa, status) values (?, ?) """, (tarefa, status))
                
                conexao.commit()
                
                print('Tarefa cadastrada com sucesso.')
                
                continuar = input('Deseja cadastrar mais tarefas? (s/n)').strip().lower()
                if continuar != 's':
                    break
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar tarefa: {erro}.')
        
def visualizar_tarefas():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                buscar = input('Digite qual tarefa está procurando: ')
                
                cursor.execute(""" SELECT * FROM tarefas WHERE tarefa = ? """, (buscar,))
                tarefa = cursor.fetchone()
                
                if tarefa:
                    print(f'Tarefa: {tarefa[1]}')
                    print(f'Status: {tarefa[2]}')
                    
                else:
                    print('Tarefa não encontrada.')
                    
                continuar = input('Deseja buscar mais tarefas? (s/n)').strip().lower()
                if continuar != 's':
                    break      
        
    except sqlite3.Error as erro:
        print(f'Erro ao buscar tarefa: {erro}.')
        
def atualizar_tarefa():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                atualizar = input('Qual tarefa deseja atualizar?')
                
                cursor.execute(""" SELECT * FROM tarefas WHERE tarefa = ? """, (atualizar,))
                tarefa = cursor.fetchone()
                
                if tarefa:
                    novo_status = input('Digite o novo status: ')
                    
                    cursor.execute(""" UPDATE tarefas SET status = ? WHERE tarefa = ? """, (novo_status, atualizar))
                    
                    conexao.commit()
                    
                    print('Status atualizado com sucesso.')
                    
                else:
                    print('Tarefa não encontrada.')
                    
                continuar = input('Deseja atualizar mais tarefas? (s/n)').strip().lower()
                if continuar != 's':
                    break
        
    except sqlite3.Error as erro:
        print(f'Erro ao atualizar tarefa: {erro}.')