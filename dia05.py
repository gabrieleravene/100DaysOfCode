# É um sistema de cadastro de pacientes desenvolvido em Python, sem interface gráfica, no qual o usuário pode:

#Cadastrar pacientes;
#Visualizar lista de pacientes já cadastrados;
#Buscar pacientes;
#Eliminar pacientes da lista.

pacientes = []

def cadastrar_pacientes():
    """ Função para cadastrar pacientes """
    
    print('Cadastro de pacientes.')
    
    nome = input('Insira o nome do paciente: ')
    
    cpf = input('Insira o CPF do paciente: ')
    
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
    
def visualizar_pacientes():
    print(pacientes)

def buscar_pacientes():
    pass

def eliminar_pacientes():
    pass