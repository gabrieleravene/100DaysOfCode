# sistema bancário

import textwrap

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        
    def criar_usuario(usuarios):
        """" Criar novos usuários """
        cpf = input('Informe o CPF (somente o número): ')
        if Usuario.filtrar_usuario(cpf, usuarios):
            print('Já existe usuário com esse CPF.')
            return None
        
        
class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.AGENCIA = "0001"
        
    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = Usuario.filtrar_usuario(cpf, self.usuarios)
        if usuario: 
            numero_conta = len(self.contas) + 1
            conta = ContaBancaria(self.AGENCIA, numero_conta, usuario)
            self.contas.append(conta)
            print("Conta criada com sucesso!")
            return conta
        print("Usuário não encontrado.")
        return None
    
    def listar_contas(self):
        for conta in self.contas:
            linha = f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.usuario.nome}
                Titular:\t{conta.usuario.nome}
                """
            print("="*100)
            print(textwrap.dedent(linha))

class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.limite = 500
        self.extrato = ""
        self.saques = 0
        self.LIMITE_SAQUES = 3
        
    def depositar(self, valor):
        """" Despositar dinheiro na conta  """
        self.saldo += valor
        print(f"Você depositou R${valor} em sua conta. Seu saldo atual é R${self.saldo}.")
        
    def sacar(self, valor):
        """" Sacar dinheiro da conta  """
        if valor > self.saldo:
            print('Você não possui saldo o suficiente para realizar esta operação.')
        elif valor > self.limite:
            print('Limite excedido para realizar esta operação.')
        elif self.saques > self.LIMITE_SAQUES:
            print('Você excedeu o limite de saques diário.')
        elif 0 > valor < self.saldo:
            self.saldo =- valor
            self.saques += 1
            print(f'Operação realizada com sucesso. Seu saldo atual é {self.saldo}.')
            
    def exibir_extrato(self):
        print("EXTRATO")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
            
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, numero_conta, saldo, taxa_juros):
        super().__init__(titular, numero_conta, saldo)
        self.taxa_juros = taxa_juros
        
    def add_juros(self, taxa_juros):
        juros = self.saldo * taxa_juros
        self.depositar(juros)