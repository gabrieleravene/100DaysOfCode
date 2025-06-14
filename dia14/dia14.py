# sistema de cadastro

import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "cadastros.db")

def criar_banco_de_dados():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS cadastro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT) """)
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def cadastrar():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                nome = input('Digite o nome: ')
                cpf = input('Digite o CPF: ')
                
                if nome:
                    break
                if cpf:
                    break
            
            cursor.execute(""" INSERT INTO cadastro (nome, cpf) values (?, ?) """, (nome, cpf))
            
            conexao.commit()
            
            print('Cadastro realizado com sucesso.')
            
    except sqlite3.Error as erro:
        print(f'Erro ao realizar cadastro: {erro}.')
        
def deletar():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                try:
                    id = int(input('Digite o ID do cadastro a ser deletado: '))
                except ValueError:
                    print('Valor inválido.')
                    
                cursor.execute(""" DELETE FROM cadastro WHERE id = ? """, (id,))
                
                conexao.commit()
                
                print('Usuário deletado com sucesso.')
                
                continuar = input('Deseja deletar mais cadastros? (s/n)').strip().lower()
                if continuar != 's':
                    break
                
    except sqlite3.Error as erro:
        print(f'Erro ao deletar cadastro: {erro}.')

def atualizar():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                try:
                    id = int(input('Digite o ID do cadastro que desejar alterar: '))
                except ValueError:
                    print('Valor inválido.')
                    
                cursor.execute(""" SELECT * FROM cadastro WHERE id = ? """, (id,))
                cadastro = cursor.fetchone()
                
                if cadastro:
                    novo_nome = input('Digite o novo nome: ')
                    
                    
                    cursor.execute(""" UPDATE cadastro SET nome = ? WHERE id = ? """, (novo_nome, id))
                    
                    conexao.commit()
                    
                    print('Cadastro alterado com sucesso.')
                    
                else:
                    print('Cadastro não encontrado.')
                
                continuar = input('Deseja alterar mais cadastros? (s/n)').strip().lower()
                if continuar != 's':
                    break
        
    except sqlite3.Error as erro:
        print(f'Erro ao atualizar cadastro: {erro}.')
