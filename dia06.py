# sistema de cadastro de exames laboratoriais

import sqlite3

def criar_banco_de_dados():
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf_paciente TEXT, 
    nome_paciente TEXT, 
    data_nascimento TEXT, 
    telefone TEXT
    )
""")

    cursor.execute("""
INSERT INTO pacientes (cpf_paciente, nome_paciente, #data_nascimento, telefone) values ('303.567.599-14', 'Beatriz #Oliveira dos Santos', '2000-02-02', '11 99294-0240'),
('400.756.284-19', 'Eduardo Pereira Carvalho', '1999-09-10','19 98234-3245'),
('450.574.234-12', 'Maria Lourdes Rodrigues', '29-11-1983', '19 98234-2345'),
('380.788.334-00', 'Luiz José Schmdit', '01-10-1970', '19 99134-7867'),
('340.325.890-01', 'Benedita Lopes', '15-05-1950', '19 #99943-0968'),
('400.005.235-12', 'Lucas Pinheiro', '18-10-2005', '19 99242-4325'),
('455.666.124-09', 'Lucia Maria Alves Pereira', '01-01-1990', '19 98832-3455'),
('394.355.967-90', 'Graziela Maria Pinto', '09-10-1997', '11 98730-0012'),
('400.000.350-11', 'Bruno Oliveira dos Santos', '10-11-2000', '19 98787-1198'),
('310.123.860-19', 'Luciano Lopes', '23-12-2001', '19 99440-0723')               
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS exames (
    exame_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf_paciente TEXT,
    nome_exame TEXT,
    data_exame TEXT,
    FOREIGN KEY(cpf_paciente) REFERENCES pacientes(cpf_paciente)
)
""")

    conexao.commit()
    
    conexao.close()

    
def buscar_paciente(cpf_paciente):
    """"Busca paciente por CPF em banco de dados"""
    
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM pacientes where cpf_paciente =?", (cpf_paciente,))
    paciente = cursor.fetchone()
    
    conexao.close()
    
    if paciente:
        return{
            "id_paciente": paciente[0],
            "cpf_paciente": paciente[1],
            "nome_paciente": paciente[2],
            "data_nascimento": paciente[3],
            "telefone": paciente[4]
        }
    else:
        print("Paciente não encontrado.")
    
def buscar_exame_por_id():
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    
    exame_id = int(input('Digite o ID do exame que deseja visualizar: '))
    
    cursor.execute("SELECT * FROM exames where exame_id = ?", (exame_id,))
    exame = cursor.fetchone()
    
    conexao.close()
    
    if exame:
            print("\nExame:")
            print(f"ID do exame: {exame[0]}")
            print(f"CPF do paciente: {exame[1]}")
            print(f"Nome do exame: {exame[2]}")
            print(f"Data do exame: {exame[3]}")
            
            continuar = input('Deseja buscar mais exames?').strip().lower()
            if continuar == 'sim':
                buscar_exame_por_id()
            else:
                menu()
    else:
        print("O exame não foi encontrado.")
        menu()

def cadastrar_exame():
    """""Cadastra exames na tabela de exames"""
    
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    
    cpf_paciente = input('Digite o CPF do paciente (XXX.XXX.XXX-XX): ')
    
    paciente = buscar_paciente(cpf_paciente)
    
    if paciente:
        print("\nPaciente:")
        print(f"Nome: {paciente['nome_paciente']}")
        print(f"CPF: {paciente['cpf_paciente']}")
        print(f"Data de nascimento: {paciente['data_nascimento']}")
        print(f"Telefone:  {paciente['telefone']}")
        
        
    exame = input('Digite o exame que você deseja cadastrar: ')
    data = input('Digite a data do exame:')
        
    cursor.execute("""
        INSERT INTO exames (cpf_paciente, nome_exame, data_exame)
        VALUES (?, ?, ?)
""", (cpf_paciente, exame, data))
    
    exame_id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    
    print(f"\nExame de {exame} cadastrado para {paciente['nome_paciente']} na data {data}. O ID do exame é {exame_id}.")
    
def eliminar_exames():
    """""Elimina exames da tabela de exames"""
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    
    exame_id = int(input('Digite o ID do exame que você deseja eliminar: '))
    
     
    cursor.execute("SELECT * FROM exames where exame_id = ?", (exame_id,))
    exame = cursor.fetchone()
    
    if exame:
        cursor.execute("DELETE FROM exames WHERE exame_id = ?", (exame_id,))
        conexao.commit()
        print("Exame excluído com sucesso.")
        
        continuar = input('Deseja eliminar mais exames?').strip().lower()
        if continuar == 'sim':
            eliminar_exames()
        else:
            menu()
    else:
        print("Exame não encontrado.")

    conexao.close()
    
def encerrar_programa():
    print("Programa encerrado.")
    
def menu():
    while True:
         print("\nSistema de cadastro de exames laboratoriais.")
         print("1 - CADASTRAR EXAMES")
         print("2 - VISUALIZAR EXAMES")
         print("3 - ELIMINAR EXAMES")
         print("4 - ENCERRAR PROGRAMA")
         
         try:
              opcao_desejada = int(input('Digite a opção desejada: '))
         except ValueError:
             print("Digite um valor númerico.")
             continue

         
         if opcao_desejada < 1 or opcao_desejada > 4:
             print("Digite uma opção válida (1-4).")
             continue

         if opcao_desejada == 1:
            cadastrar_exame()
         elif opcao_desejada == 2:
            buscar_exame_por_id()
         elif opcao_desejada == 3:
            eliminar_exames()
         elif opcao_desejada == 4:
            encerrar_programa()
            return
         else:
            print('Digite uma opção válida.')
            opcao_desejada = int(input('Digite a opção desejada: '))