# sistema de cadastro

import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "pacienteslab.db")

def criar_banco_de_dados():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS pacients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT,
                telefone TEXT) """)
    
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def cadastrar_paciente():
    try:
        with sqlite3.connect("pacienteslab.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                nome_paciente = input('Digite o nome do paciente: ')
                cpf_paciente = input('Digite o CPF do paciente: ')
                telefone_paciente = input('Digite o telefone do paciente: ')
                
                cursor.execute(""" INSERT INTO pacients (nome, cpf, telefone) values (?, ?, ?) """, (nome_paciente, cpf_paciente, telefone_paciente,))
                
                conexao.commit()
                
                print('Paciente cadastrado com sucesso!')
                
                continuar = input('Deseja cadastrar mais pacientes?').strip().lower()
                if continuar != 's':
                    return 
        
    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar paciente: {erro}.')
        
def visualizar_paciente():
    try:
        with sqlite3.connect("pacienteslab.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                id_paciente = input('Digite o ID do paciente que deseja visualizar os dados: ')
                
                cursor.execute(""" SELECT * FROM pacients WHERE id = ?""", (id_paciente,))
                paciente = cursor.fetchone()
                
                if paciente:
                    print("\nPaciente:")
                    print(f"ID: {paciente[0]}")
                    print(f"Nome: {paciente[1]}")
                    print(f"CPF: {paciente[2]}")
                    print(f"Telefone: {paciente[3]}")
                    
                else:
                    print('Paciente não encontrado.')
                    
                continuar = input('Deseja continuar? (s/n)')
                if continuar != 's':
                    return
        
    except sqlite3.Error as erro:
        print(f'Erro ao buscar paciente: {erro}.')
        

def alterar_dados():
    try:
        with sqlite3.connect("pacienteslab.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                id_paciente = input('Digite o ID do paciente que deseja alterar os dados: ')
                
                cursor.execute(""" SELECT * FROM pacients WHERE id = ? """, (id_paciente,))
                paciente = cursor.fetchone()
                
                if paciente:
                    print("\nPaciente:")
                    print(f"Nome: {paciente[1]}")
                    print(f"CPF: {paciente[2]}")
                    print(f"Telefone: {paciente[3]}")
                    
                    alterar = input('O que deseja alterar? (nome/cpf/telefone)').strip().lower()
                    if alterar == 'nome':
                        alteracao = input('Digite alteração a ser feita: ')
                        
                        cursor.execute(""" UPDATE pacients SET nome = ? WHERE id = ? """, (alteracao, id_paciente))
                        
                        conexao.commit()
                    
                        print('Dados foram alterados com sucesso!')
                        
                        
                    elif alterar == 'cpf':
                        alteracao = input('Digite alteração a ser feita: ')
                        
                        cursor.execute(""" UPDATE pacients SET cpf = ? WHERE id = ? """, (alteracao, id_paciente))
                        
                        conexao.commit()
                    
                        print('Dados foram alterados com sucesso!')
                        
                    elif alterar == 'telefone':
                        alteracao = input('Digite a alteração a ser feita: ')
                        
                        cursor.execute(""" UPDATE pacients SET telefone = ? WHERE id = ? """, (alteracao, id_paciente))
                        
                        conexao.commit()
                    
                        print('Dados foram alterados com sucesso!')
                    
                    else:
                        print('Opção inválida.')
                    
                else:
                    print('Paciente não encontrado.')
                    
                    
                continuar = input('Deseja continuar? (s/n)')
                if continuar != 's':
                    return
        
    except sqlite3.Error as erro:
        print(f'Erro ao alterar dados: {erro}.')        

def deletar_cadastro():
    try:
        with sqlite3.connect("pacienteslab.db") as conexao:
            cursor = conexao.cursor()
            
            while True:
                id_cadastro = input('Digite o ID do cadastro que deseja remover: ')
                
                cursor.execute(""" SELECT * FROM pacients WHERE id = ? """, (id_cadastro,))
                paciente = cursor.fetchone()
                
                if paciente:
                    print("\nPaciente:")
                    print(f"ID: {paciente[0]}")
                    print(f"Nome: {paciente[1]}")
                    print(f"CPF: {paciente[2]}")
                    print(f"Telefone: {paciente[3]}")
                    
                    confirma = input('Deseja realmente deletar esse cadastro? (s/n)')
                    if confirma == 's':
                        cursor.execute(""" DELETE FROM pacients WHERE id = ? """, (id_cadastro,))
                        
                        conexao.commit()
                        
                        print('Cadastro removido com sucesso.')         
                    
                else:
                    print('Paciente não encontrado.')
                          
                continuar = input('Deseja remover mais cadastros? (s/n)').strip().lower()
                if continuar != 's':
                    return
        
    except sqlite3.Error as erro:
        print(f'Erro ao deletar paciente: {erro}.')
        
def menu():
    while True:
       print("\nSistema de cadastro de pacientes.")
       print("1 - Cadastrar paciente")
       print("2 - Visualizar cadastro")
       print("3 - Alterar cadastro")
       print("4 - Remover cadastro")
       print("5 - Encerrar o programa")
    
       opcao = input('Digite a ação desejada: ')
       if opcao == '1':
         cadastrar_paciente()
       elif opcao == '2':
         visualizar_paciente()
       elif opcao == '3':
        alterar_dados()
       elif opcao == '4':
        deletar_cadastro()
       elif opcao == '5':
          print('Programa encerrado.')
          break
       else:
          print('Opção inválida. Tente novamente.')
        
if __name__ == "__main__":
    criar_banco_de_dados()
    menu()