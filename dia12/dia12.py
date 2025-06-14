# sistema de cadastro

import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "cadastros.db")

def criar_banco_de_dados():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS cadastros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                data_nascimento TEXT,
                cpf TEXT) """) 
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def cadastrar():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                nome = input('Digite o nome: ')
                data_nascimento = input('Digite a data de nascimento: ')
                cpf = input('Digite o CPF: ')
                
                if nome and data_nascimento and cpf:
                    break
            
            cursor.execute(""" INSERT INTO cadastros (nome, data_nascimento, cpf) values (?, ?, ?) """, (nome, data_nascimento, cpf))
            
            print('Cadastro realizado com sucesso.')
            
            conexao.commit()               
        
    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar usuário: {erro}.')

def deletar():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                try:
                    id = int(input('Digite o ID do usuario que deseja deletar: '))
                except ValueError:
                    print('Valor inválido.')
                    
                cursor.execute(""" DELETE FROM cadastros WHERE id = ? """, (id,))
                
                conexao.commit()
                
                print('Cadastro deletado.')
                    
                continuar = input('Deseja deletar mais cadastros? (s/n)')
                if continuar != 's':
                    break
                
    except sqlite3.Error as erro:
        print(f'Erro ao deletar cadastro: {erro}.')