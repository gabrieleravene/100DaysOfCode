import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "listadecompras.db")


def criar_banco_de_dados():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS compras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT,
                quantidade INTEGER,
                categoria TEXT) """)
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def adicionar_itens():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                try:
                   item = input('Digite o item: ')
                   qtde = int(input('Digite a quantidade: '))
                   cat = input('Digite a categoria (alimentação/limpeza/variados): ')
                except ValueError:
                    print('Digite um valor válido.')
                    
                cursor.execute(""" INSERT INTO compras (item, quantidade, categoria) values (?, ?, ?) """, (item, qtde, cat))
                
                conexao.commit()
                
                print('Item cadastrado com sucesso.')
                
                continuar = input('Deseja cadastrar mais itens?').strip().lower()
                if continuar != 's':
                    break
        
    except sqlite3.Error as erro:
        print(f'Erro ao adicionar item a lista de compras: {erro}.')
        

def visualizar_lista():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" SELECT * FROM compras """)
            lista = cursor.fetchall()
            
            for item in lista:
                print(f"ID: {item[0]} - Item: {item[1]} - Quantidade: {item[2]} - Categoria: {item[3]}")
        
    except sqlite3.Error as erro:
        print(f'Erro ao buscar itens: {erro}.')
        
def menu():
    while True:
        print('1 - Adicionar itens a lista')
        print('2 - Visualizar lista')
        print('3 - Encerrar programa')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            adicionar_itens()
        elif opcao == 2:
            visualizar_lista()
        elif opcao == 3:
            print('Programa encerrado.')
            break
        else:
            print('Valor inválido.')
            
