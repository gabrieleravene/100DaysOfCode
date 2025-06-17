import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "biblioteca.db")

def criar_banco_de_dados():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS biblioteca (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                autor TEXT,
                status TEXT) """)
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def cadastrar_livro():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                titulo = input('Digite o título do livro: ')
                autor = input('Digite o nome do autor: ')
                status = input('Digite o status do livro: ')
                
                cursor.execute(""" INSERT INTO biblioteca (titulo, autor, status) values (?, ?, ?) """, (titulo, autor, status))
                
                conexao.commit()
                
                print('Livro cadastrado com sucesso.')
                
                continuar = input('Deseja cadastrar mais livros? (s/n)').strip().lower()
                if continuar != 's':
                    break
        
    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar livro: {erro}.')
        
def visualizar_biblioteca():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" SELECT * FROM biblioteca """)
            biblioteca = cursor.fetchall()
            
            for livros in biblioteca:
                print(f'ID: {livros[0]} - Título: {livros[1]} - Autor: {livros[2]} - Status: {livros[3]}')
    
    except sqlite3.Error as erro:
        print(f'Erro ao buscar banco de dados: {erro}.')
        
def menu():
    while True:
        print('1 - Cadastrar livros')
        print('2 - Visualizar biblioteca')
        print('3 - Encerrar programa')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            cadastrar_livro()
        elif opcao == 2:
            visualizar_biblioteca()
        elif opcao == 3:
            print('Programa encerrado.')
            break
        else:
            print('Valor inválido.')