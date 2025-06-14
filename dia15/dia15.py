# sistema de cadastro de pacientes no qual o usuário pode:

pacientes = []

def cadastrar_pacientes():
    """ Função para cadastrar pacientes """
    
    print('Cadastro de pacientes.')
    
    nome = input('Insira o nome do paciente: ')
    
    cpf = input('Insira o CPF do paciente: ')
    existe = any(paciente["cpf"] == cpf for paciente in pacientes)
    if existe == True:
        print('O paciente já está cadastrado.')
        menu()
    
    dn = input('Insira a data de nascimento do paciente: ')
    
    contato = input('Insira o contato do paciente: ')
    
    paciente = {
        "nome":nome,
        "cpf":cpf,
        "data_nascimento":dn,
        "contato":contato
    }
    
    pacientes.append(paciente)
    
    print("Paciente cadastrado com sucesso.")
    
    mais_cadastros = input('Deseja cadastrar mais pacientes?').strip().lower()
    if mais_cadastros == 'sim':
        cadastrar_pacientes()
    else:
        escolha = input('Digite 1 para retornar ao menu ou 2 para encerrar o programa.').strip()
        if escolha == '1':
            menu()
        else:
            encerrar_programa()
        
    
def visualizar_pacientes():
    """Função para visualizar lista de pacientes"""
    print("Lista de pacientes cadastrados.")
    for p, paciente in enumerate(pacientes, start=1):
        print(f"\nPaciente {p}:")
        for chave, valor in paciente.items():
            print(f"{chave.capitalize()}: {valor}")

    escolha = input('Digite 1 para retornar ao menu ou 2 para encerrar o programa.').strip()
    if escolha == '1':
        menu()
    else:
        encerrar_programa()
        

def buscar_pacientes():
    """ Função para buscar pacientes """
    pesquisa = input('Digite o CPF do paciente que deseja visualizar os dados: ').strip()
    paciente_encontrado = next((p for p in pacientes if p.get("cpf") == pesquisa), None)
    
    if paciente_encontrado:
        print("Paciente encontrado:")
        for chave, valor in paciente_encontrado.items():
            print(f"{chave.capitalize()}: {valor}")
    else:
        print("Paciente não encontrado.")
            
    escolha = input('Digite 1 para retornar ao menu ou 2 para encerrar o programa.').strip()
    if escolha == '1':
        menu()
    else:
        encerrar_programa()
    

def eliminar_pacientes():
    """ Função para eliminar pacientes """
    pesquisa = input('Digite o CPF do paciente que você deseja eliminar: ').strip()
    paciente_eliminado = next((p for p in pacientes if p.get("cpf") == pesquisa), None)
    
    if paciente_eliminado:
        for chave, valor in paciente_eliminado.items():
            print(f"{chave.capitalize()}: {valor}")
        confirmacao = input('Deseja realmente eliminar este paciente?').strip().lower()
        if confirmacao == 'sim':
            pacientes.remove(paciente_eliminado)
            print('Paciente eliminado.')
            escolha = input('Digite 1 para retornar ao menu ou 2 para encerrar o programa.').strip()
            if escolha == '1':
                menu()
            else:
                encerrar_programa()
        else:
            escolha = input('Digite 1 para retornar ao menu ou 2 para encerrar o programa.').strip()
            if escolha == '1':
                menu()
            else:
                encerrar_programa()
                
    

def encerrar_programa():
    """ Função que imprime na tela a mensagem de que o programa foi encerrado """
    print('Programa encerrado.')

def menu():
    """ Função que exibe na tela um menu com as opções para o usuário escolher o que fazer """
    print('Sistema de cadastro de pacientes.\n'
          '1 - CADASTRAR PACIENTES\n'
          '2 - VISUALIZAR PACIENTES CADASTRADOS \n'
          '3 - ELIMINAR CADASTRO DE PACIENTE\n'
          '4 - BUSCAR PACIENTES\n'
          '5 - ENCERRAR PROGRAMA')
    opcao_desejada = input('Digite a opção desejada: ').strip()
    if opcao_desejada == '1':
        cadastrar_pacientes()
    elif opcao_desejada == '2':
        visualizar_pacientes()
    elif opcao_desejada == '3':
        eliminar_pacientes()
    elif opcao_desejada == '4':
        buscar_pacientes()
    else:
        encerrar_programa()