import sqlite3
import os

script_diretorio = os.path.dirname(__file__)

caminho_db = os.path.join(script_diretorio, "db", "funcionarios.db")

def criar_banco_de_dados():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cargo TEXT NOT NULL,
                turno TEXT NOT NULL,
                data_entrada DATE NOT NULL,
                status TEXT NOT NULL) """)
        
    except sqlite3.Error as erro:
        print(f'Erro ao criar banco de dados: {erro}.')
        
def cadastrar_funcionario():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                nome = input('Digite o nome do funcionário: ')
                cargo = input('Digite o cargo do funcionário (coletador/técnico/analista): ')
                turno = input('Digite o turno do funcionário (integral/diurno/noturno): ')
                data_entrada = input('Digite a data de entrada (DD-MM-AA): ')
                status = input('Digite o status do funcionário (ativo/inativo/afastado/demitido/em treinamento): ')
                
                cursor.execute(""" INSERT INTO funcionarios (nome, cargo, turno, data_entrada, status) values (?, ?, ?, ?, ?) """, (nome, cargo, turno, data_entrada, status))
                
                conexao.commit()
                
                print('Funcionário cadastrado com sucesso!')
                
                continuar = input('Deseja cadastrar mais funcionários?')
                if continuar != 's':
                    return
                     
    except sqlite3.Error as erro:
        print(f'Erro ao cadastrar funcionário: {erro}.')
        
        
def filtrar_cargo_ou_turno():
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                busca = input('Digite o que deseja filtrar (cargo/turno): ').strip().lower()
                if busca == 'cargo':
                    cargo = input('Digite o cargo que deseja filtrar (coletador/técnico/analista): ').strip().lower()
                    if cargo == 'coletador':
                        cursor.execute(""" SELECT * FROM funcionarios WHERE LOWER(cargo) = ? """, (cargo,))
                        funcionarios = cursor.fetchall()
                        
                        if funcionarios:
                            for func in funcionarios:
                                print(f"ID: {func[0]} - Nome: {func[1]} - Cargo: {func[2]} - Turno: {func[3]} - Data de entrada: {func[4]} - Status: {func[5]}")
                                
                        else:
                            print('Nenhum funcionário encontrado.')
                            
                    elif cargo == 'técnico':
                        cursor.execute(""" SELECT * FROM funcionarios WHERE LOWER(cargo) = ? """, (cargo,))
                        funcionarios = cursor.fetchall()
                        
                        if funcionarios:
                            for func in funcionarios:
                                print(f"ID: {func[0]} - Nome: {func[1]} - Cargo: {func[2]} - Turno: {func[3]} - Data de entrada: {func[4]} - Status: {func[5]}")
                                
                        else:
                            print('Nenhum funcionário encontrado para esse turno.')
                            
                    elif cargo == 'analista':
                        cursor.execute(""" SELECT * FROM funcionarios WHERE LOWER(cargo) = ? """, (cargo,))
                        funcionarios = cursor.fetchall()
                        
                        if funcionarios:
                            for func in funcionarios:
                                print(f"ID: {func[0]} - Nome: {func[1]} - Cargo: {func[2]} - Turno: {func[3]} - Data de entrada: {func[4]} - Status: {func[5]}")
                                
                            else:
                                print('Nenhum funcionário encontrado.')
                                
                elif busca == 'turno':
                    turno = input('Digite o turno (integral/diurno/noturno: )').strip().lower()
                    if turno == 'integral':
                        cursor.execute(""" SELECT * FROM funcionarios WHERE LOWER(turno) = ? """, (turno,))
                        funcionarios = cursor.fetchall()
                        
                        if funcionarios:
                            for func in funcionarios:
                                print(f"ID: {func[0]} - Nome: {func[1]} - Cargo: {func[2]} - Turno: {func[3]} - Data de entrada: {func[4]} - Status: {func[5]}")
                        else:
                            print('Nenhum funcionário encontrado para esse turno.')
                            
                    elif turno == 'diurno':
                        cursor.execute(""" SELECT * FROM funcionarios WHERE LOWER(turno) = ? """, (turno,))
                        funcionarios = cursor.fetchall()
                        
                        if funcionarios:
                            for func in funcionarios:
                                 print(f"ID: {func[0]} - Nome: {func[1]} - Cargo: {func[2]} - Turno: {func[3]} - Data de entrada: {func[4]} - Status: {func[5]}")
                        else:
                            print('Nenhum funcionário encontrado para esse turno.')
                            
                    elif turno == 'noturno':
                        cursor.execute(""" SELECT * FROM funcionarios WHERE LOWER(turno) = ? """, (turno,))
                        funcionarios = cursor.fetchall()
                        
                        if funcionarios:
                            for func in funcionarios:
                                print(f"ID: {func[0]} - Nome: {func[1]} - Cargo: {func[2]} - Turno: {func[3]} - Data de entrada: {func[4]} - Status: {func[5]}")
                        else:
                            print('Nenhum funcionário encontrado para esse turno.')
                            
                else:
                        print('Opção inválida.')
                        
                continuar = input('Deseja buscar mais dados? (s/n)').strip().lower()
                if continuar != 's':
                   return
                                
    except sqlite3.Error as erro:
        print(f'Erro ao filtrar dados: {erro}.')

def alterar_status():
    """ Função para alterar função do funcionário na empresa """
    try:
        with sqlite3.connect(caminho_db) as conexao:
            cursor = conexao.cursor()
            
            while True:
                alterar = input('Digite o nome do funcionário que deseja alterar o status: ')
                
                cursor.execute(""" SELECT * FROM funcionarios WHERE nome = ? """, (alterar,))
                funcionario = cursor.fetchone()
                
                if funcionario:
                    alteracao = input('Digite a mudança de status: ')
                    cursor.execute(""" UPDATE funcionarios SET status = ? WHERE nome = ? """, (alteracao, alterar))
                    
                    conexao.commit()
                    
                    print('Status alterado com sucesso!')
                    
                else:
                    print('Funcionário não encontrado.')
                    
                continuar = input('Deseja alterar mais dados? (s/n)').strip().lower()
                if continuar != 's':
                    return
        
    except sqlite3.Error as erro:
        print(f'Erro ao alterar status do funcionário na empresa: {erro}.')
        
def menu():
    while True:
        print('Sistema de cadastro de funcionários.')
        print('1 - Cadastrar funcionário')
        print('2 - Filtrar por cargo ou turno')
        print('3 - Alterar status do funcionário')
        print('4 - Encerrar programa')
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            cadastrar_funcionario()
        elif opcao == 2:
            filtrar_cargo_ou_turno()
        elif opcao == 3:
            alterar_status()
        elif opcao == 4:
            print('Encerrando programa...')
        else:
            print('Opção inválida.')