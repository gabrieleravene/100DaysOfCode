# sistema de cadastro de exames

import sqlite3

def criar_banco_de_dados():
    conexao = sqlite3.connect("exames.db")
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bioquimica (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_paciente TEXT,
            nome_exame TEXT
        )
    """)
    
    conexao.commit()
    conexao.close()
    
def cadastrar_exames():
    conexao = sqlite3.connect("exames.db")
    cursor = conexao.cursor()
    
    nome_paciente = input('Digite o nome completo do paciente: ')
    nome_exame = input('Digite o nome do exame que deseja cadastrar para o paciente: ')
    
    cursor.execute("""
        INSERT INTO bioquimica (nome_paciente, nome_exame)
        values (?, ?)
    """, (nome_paciente, nome_exame))
    
    conexao.commit()
    conexao.close()
    
    print("O exame foi cadastrado!")