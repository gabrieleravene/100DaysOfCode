# sistema de cadastro de pacientes

import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "dbpacientes.db")

def criar_banco_de_dados():
    """" Função para criar banco de dados """
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nome TEXT,
                cpf TEXT) """)
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def cadastrar_paciente():
    """" Função para cadastrar paciente """
    try:
        with sqlite3.connect("dbpacientes.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                try:
                    nome = input('Digite o nome do paciente: ')
                    cpf = input('Digite o CPF do paciente: ')
                    
                    cursor.execute(""" INSERT INTO pacientes values (?, ?, ?) """, (None, nome, cpf))
                    
                    conexao.commit()
                    
                    print('O paciente foi cadastrado com sucesso.')
                    
                    continuar = input('Deseja continuar? (s/n)').strip().lower()
                    if continuar != 's':
                        return
                
                except ValueError:
                    print(f'Insira um valor válido.')
            
        
    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar paciente: {erro}.')
        

def buscar_paciente():
    """" Função para buscar paciente em banco de dados """
    try:
        with sqlite3.connect("dbpacientes.db") as conexao:
            cursor = conexao.cursor()
            
            try:
                cpf = input('Digite o CPF do paciente: ')
                
                cursor.execute(""" SELECT * FROM pacientes where cpf = ? """, (cpf,))
                paciente = cursor.fetchone()
                
                if paciente:
                    {
                     "id":paciente[0],
                     "nome": paciente[1],
                     "cpf":paciente[2]}
                    print('Paciente encontrado.')
                    
                else:
                    print('Paciente não encontrado.')
                
            except ValueError:
                print('Insira um valor válido.')
    
    except sqlite3.Error as erro:
        print(f'Erro ao buscar paciente: {erro}.')