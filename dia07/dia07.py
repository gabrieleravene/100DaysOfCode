# sistema de controle de estoque de insumos de laboratório

import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "insumos.db")

def criar_banco_de_dados():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                unidade TEXT NOT NULL,
                data_validade DATE,
                data_entrada DATE NOT NULL) """)
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')

def cadastrar_insumos():
    print('Cadastro de insumos.')
    try:
        with sqlite3.connect("insumos.db") as conexao:
            cursor = conexao.cursor()
             

            while True:
                try:
                  nome = input('Digite o nome do insumo: ')
                  tipo = input('Digite o tipo de insumo: ')
                  qtde = int(input('Digite a quantidade: '))
                  un = input('Digite a unidade: ')
                  val = input('Digite a data de validade: ')
                  entrada = input('Digite a data de entrada: ')
                
                  cursor.execute(""" INSERT INTO estoque (id, nome, tipo, quantidade, unidade, data_validade, data_entrada) values (?, ?, ?, ?, ?, ?, ?) """, (None, nome, tipo, qtde, un, val, entrada),)
                  conexao.commit()
                
                  print('Insumo cadastrado com sucesso.')
                
                except ValueError:
                  print('Valor inválido.')
                  
                continuar = input('Deseja cadastrar mais insumos? (s/n)')
                if continuar != 's':
                    return

        
    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar insumo: {erro}.')

def visualizar_insumos():
    print('Visualizar dados de insumos.')
    try:
        with sqlite3.connect("insumos.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
               buscar = input('Digite o nome do insumo que deseja buscar: ')
               
               cursor.execute(""" SELECT * FROM estoque WHERE nome = ? """, (buscar,))
               insumo = cursor.fetchone()
               
               if insumo:
                   print(f"ID: {insumo[0]}")
                   print(f"Nome: {insumo[1]}")
                   print(f"Tipo: {insumo[2]}")
                   print(f"Quantidade:: {insumo[3]}")
                   print(f"Unidade: {insumo[4]}")
                   print(f"Data de validade: {insumo[5]}")
                   print(f"Data de entrada: {insumo[6]}")
                
               else:
                   print('Insumo não encontrado.')
                   
                
               continuar = input('Deseja buscar mais insumos? (s/n)')
               if continuar != 's':
                    return
            
    except sqlite3.Error as erro:
        print(f'Erro ao buscar insumos: {erro}.')
        
def atualizar_info():
    try:
        with sqlite3.connect("insumos.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                nome = input('Digite o nome do insumo que deseja alterar: ')
                
                cursor.execute(""" SELECT * FROM estoque WHERE nome = ? """, (nome,))
                insumo = cursor.fetchone()
                
                if insumo:
                    print(f"ID: {insumo[0]}")
                    print(f"Nome: {insumo[1]}")
                    print(f"Tipo: {insumo[2]}")
                    print(f"Quantidade: {insumo[3]}")
                    print(f"Unidade: {insumo[4]}")
                    print(f"Data de validade: {insumo[5]}")
                    print(f"Data de entrada: {insumo[6]}")
                    
                    alterar = input('O que deseja alterar? (quantidade/data de validade): ').strip().lower()
                    if alterar == 'quantidade':
                        nova_qtde = int(input('Digite a nova quantidade: '))
                        
                        cursor.execute(""" UPDATE estoque SET quantidade = ? WHERE nome = ?  """, (nova_qtde, nome))
                        
                        conexao.commit()
                        
                        print('Quantidade alterada com sucesso!')
                    
                    elif alterar == 'data de validade':
                        nova_val = input('Digite a nova data de validade: ')
                        
                        cursor.execute(""" UPDATE estoque SET data_validade = ? WHERE nome = ? """, (nova_val, nome))
                        
                        conexao.commit()
                        
                        print('Data de validade alterada com sucesso!')
                
                else:
                    print('Insumo não encontrado.')
                        
                    continuar = input('Deseja alterar mais dados?').strip().lower()
                    if continuar != 's':
                        return
                              
    except sqlite3.Error as erro:
        print(f"Erro ao atualizar dados: {erro}.")
        

def deletar_insumos():
    try:
        with sqlite3.connect("insumos.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                deletar = input('Digite o nome do insumo que deseja deletar: ')
                
                cursor.execute(""" SELECT * FROM estoque WHERE nome = ? """, (deletar,))
                insumo = cursor.fetchone()
                
                if insumo:
                    print(f"ID: {insumo[0]}")
                    print(f"Nome: {insumo[1]}")
                    print(f"Tipo: {insumo[2]}")
                    print(f"Quantidade: {insumo[3]}")
                    print(f"Unidade: {insumo[4]}")
                    print(f"Data de validade: {insumo[5]}")
                    print(f"Data de entrada: {insumo[6]}")
                    
                    confirma = input('Deseja realmente deletar esse insumo? (s/n)').strip().lower()
                    if confirma == 's':
                        cursor.execute(""" DELETE FROM estoque WHERE nome = ? """, (deletar,))
                        
                        conexao.commit()
                        
                        print('Insumo deletado com sucesso!')
                        
                else:
                    print('Insumo não encontrado.')
                        
                continuar = input('Deseja deletar mais insumos? (s/n)').strip().lower()
                if continuar != 's':
                    return
                        
        
    except sqlite3.Error as erro:
        print(f'Erro ao deletar insumo: {erro}.')
        

def menu():
    while True:
        print('Sistema de controle de estoque de insumos de laboratório.')
        print("\n1 - Cadastrar insumo")
        print("2 - Visualizar informações sobre insumo")
        print("3 - Alterar informações sobre insumo")
        print("4 - Deletar insumo da tabela")
        print("5 - Encerrar programa")
        opcao = int(input('Digite a opçao desejada: '))
        if opcao == 1:
            cadastrar_insumos()
        elif opcao == 2:
            visualizar_insumos()
        elif opcao == 3:
            atualizar_info()
        elif opcao == 4:
            deletar_insumos()
        elif opcao == 5:
            print("Encerrando programa...")
            break