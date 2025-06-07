# sistema de cadastro de pacientes

import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "pacientes.db")

def criar_banco_de_dados():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT) """)  
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def cadastrar_paciente():
    try:
        with sqlite3.connect("pacientes.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                try:
                    nome = input('Digite o nome do paciente: ')
                    cpf = input('Digite o CPF do paciente: ')
                    
                    cursor.execute(""" INSERT INTO pacientes (nome, cpf) values (?, ?) """, (nome, cpf))
                    
                    conexao.commit()
                    
                    print('O paciente foi cadastrado com sucesso.')
                    
                    continuar = input('Deseja cadastrar mais pacientres?')
                    if continuar != 's':
                        return
                    
                except ValueError:
                    print('Digite um valor válido.')
                      
    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar paciente no banco de dados: {erro}.')
