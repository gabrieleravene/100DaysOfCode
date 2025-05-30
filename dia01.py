# sistema de cadastro de alunos

import sqlite3

def criar_banco_de_dados():
    try:
        with sqlite3.connect("alunos.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT
            )
            """)
        
    except sqlite3.Error as erro:
        print(f"Erro ao criar banco de dados: {erro}.")

def cadastrar_alunos():
    try:
        with sqlite3.connect("alunos.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                try:
                   nome = input('Digite o nome do aluno: ')
                   cpf = input('Digite o CPF do aluno: ')
                
                   cursor.execute("""  INSERT INTO alunos (nome, cpf) values (?, ?) """, (nome, cpf))
                
                   conexao.commit()
                
                   print('O aluno foi cadastrado com sucesso.')
                
                   continuar = input('Deseja cadastrar mais produtos? (s/n)').strip().lower()
                
                   if continuar != 's':
                       return
                
                except ValueError:
                  print("Digite um valor válido.")
    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar aluno: {erro}.')
        
cadastrar_alunos()
                
            