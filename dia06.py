# sistema de cadastro de exames laboratoriais

import sqlite3

conn = sqlite3.connect("pacientes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE pacientes (cpf, nome, data_nascimento, telefone)       
""")

cursor.execute("""
INSERT INTO pacientes (cpf, nome, data_nascimento, telefone) values #('303.567.599-14', 'Beatriz Oliveira dos Santos', '2000-02-02', '11 #99294-0240'),
('400.756.284-19', 'Eduardo Pereira Carvalho', '1999-09-10','19 98234-3245'),
('450.574.234-12', 'Maria Lourdes Rodrigues', '29-11-1983', '19 98234-2345'),
('380.788.334-00', 'Luiz José Schmdit', '01-10-1970', '19 99134-7867'),
('340.325.890-01', 'Benedita Lopes', '15-05-1950', '19 99943-0968'),
('400.005.235-12', 'Lucas Pinheiro', '18-10-2005', '19 99242-4325'),
('455.666.124-09', 'Lucia Maria Alves Pereira', '01-01-1990', '19 98832-3455'),
('394.355.967-90', 'Graziela Maria Pinto', '09-10-1997', '11 98730-0012'),
('400.000.350-11', 'Bruno Oliveira dos Santos', '10-11-2000', '19 98787-1198'),
('310.123.860-19', 'Luciano Lopes', '23-12-2001', '19 99440-0723')
""")

cursor.execute("""
CREATE TABLE exames (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf_paciente TEXT,
    nome_exame TEXT,
    data_exame TEXT, 
    FOREIGN KEY(cpf_paciente) REFERENCES pacientes(cpf)
)   
""")

conn.commit()
conn.close()


def buscar_paciente_por_cpf(cpf):
    """ Função para buscar paciente por CPF em banco de dados """
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM pacientes where cpf =?", (cpf,))
    paciente = cursor.fetchone()
    
    conexao.close()
    
    if paciente:
        return{
            "cpf": paciente[0],
            "nome":paciente[1],
            "data_nascimento":paciente[2],
            "telefone":paciente[3]
        }
        
    else:
        return None
    
def buscar_exame_por_id(id_exame):
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM exames where id =?", (id_exame,))
    exame = cursor.fetchone()
    
    conexao.close()
    
    if exame:
        return{
            "id": exame[0],
            "cpf": exame[1],
            "nome": exame[2],
            "data": exame[3]
        }
    else:
        return None

def cadastrar_exames():
    """ Função para cadastrar exames na tabela exames """
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    
    cpf_paciente = input('Digite o CPF do paciente: ')
    
    paciente = buscar_paciente_por_cpf(cpf_paciente)
    
    if paciente:
        print("\nPaciente:")
        print(f"Nome: {paciente['nome']}")
        print(f"CPF: {paciente['cpf']}")
        print(f"Data de Nascimento: {paciente['data_nascimento']}")
        print(f"Telefone: {paciente['telefone']}\n")
             
    exame = input('Digite o exame que você deseja cadastrar: ')
    data = input('Digite a data do exame: ')
    
    cursor.execute("""
    INSERT INTO exames (cpf_paciente, nome_exame, data_exame)
    VALUES (?, ?, ?) 
    """, (cpf_paciente, exame, data))
    
    conexao.commit()
    conexao.close()
    print(f"\nExame de {exame} cadastrado para {paciente['nome']} na data {data}.")
    menu()
    

def buscar_exames():   
    id_exame = input('Digite o ID do exame: ')
    
    try:
        id_exame = int(id_exame)
    except ValueError:
        print("\nID inválido.")
        return
    
    exame = buscar_exame_por_id(id_exame)
    
    if exame:
        print("\nExame:")
        print(f"ID: {exame['id']}")
        print(f"CPF do paciente: {exame['cpf']}")
        print(f"Nome do exame: {exame['nome']}")
        print(f"Data do exame: {exame['data']}\n")
    else:
        print("\n Exame não encontrado.")

def eliminar_exames():
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    
    try:
        id_exame = input('Digite a solicitação do exame: ')
    except ValueError:
        print("Solicitação inválida. Digite um número válido.")
        conexao.close()
    
    exame = buscar_exame_por_id(id_exame)
    
    if exame:
        confirmacao = input('Tem certeza que deseja eliminar esse exame?').strip().lower()
        if confirmacao == 'sim':
            cursor.execute("DELETE FROM exames WHERE id=?", (id_exame,))
            conexao.commit()
            print('O exame foi eliminado com sucesso.')
        else:
            print('Ação cancelada.')  
            
    conexao.close()
    menu()
            
def encerrar_programa():
    print("Programa encerrado.")

def menu():
    print("\n Sistema de Cadastro de Exames Laboratoriais")
    print("1 - Cadastrar exame")
    print("2 - Buscar exames")
    print("3 - Eliminar exames")
    print("4 - Encerrar programa.")
        
    try:
        opcao_desejada = int(input('Digite  a opção desejada: '))
        if 1 <= opcao_desejada <= 4:
            if opcao_desejada == 1:
                cadastrar_exames()
            elif opcao_desejada == 2:
                buscar_exames()
            elif opcao_desejada == 3:
                eliminar_exames()
            elif opcao_desejada == 4:
               encerrar_programa()
        else:
            print("Opção inválida.")
            menu()
    except ValueError:
        print("Opção inválida. Digite um número válido.")
        menu()