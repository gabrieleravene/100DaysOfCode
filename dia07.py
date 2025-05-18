# sistema de cadastro de pacientes

import sqlite3

def criar_banco_de_dados():
    conexao = sqlite3.connect("dbpacientes.db")
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dbpacientes (
            if_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf_paciente TEXT,
            nome_paciente TEXT
        )
    """)
    
    conexao.commit()
    conexao.close()
    
    
def cadastrar_paciente():
    conexao = sqlite3.connect("dbpacientes.db")
    cursor = conexao.cursor()
    
    cpf = input("Digite o CPF do paciente: ")
    nome = input('Digite o nome completo do paciente: ')

    
    cursor.execute("""
        INSERT INTO dbpacientes (cpf_paciente, nome_paciente) 
        values (?, ?)
    """, (cpf, nome))
    
    conexao.commit()
    conexao.close()
    
    print("Paciente cadastrado com sucesso.")
    
