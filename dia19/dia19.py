# sistema bancário básico - poo

class Usuario:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        
    def criar_usuario(usuarios):
        cpf = input('Informe o CPF: ')
        if Usuario.filtrar_usuario(cpf, usuarios):
            print('Já existe usuário com esse CPF.')
            return None
        
    def filtrar_usuario(cpf, usuarios):
        for usuario in usuarios:
            if usuario.cpf == cpf:
                return usuario
            return None

class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"O {self.titular} adicionou R${valor}. O saldo da conta agora é: {self.saldo}.")
        else:
            print('Valor inválido.')
        
    def sacar(self, valor):
        if valor > self.saldo:
            print("Operação falhou. Você não possui saldo o suficiente.")
        elif valor > self.limite:
            print("Operação falhou. O valor do saque excede o limite.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Operação falhou. Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\R$ {valor:2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso.")
        else:
            print('Valor inválido.')
            
class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.AGENCIA = "0001"
        
def criar_conta(self):
    cpf = input('Informe o CPF do usuário: ')
    usuario = Usuario.filtrar_usuario(cpf, self.usuarios)
    if usuario:
        numero_conta = len(self.contas) + 1
        self.contas.append(conta)
        
            
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, numero_conta, saldo, taxa_juros):
        super().__init__(titular, numero_conta, saldo)
        self.taxa_juros = taxa_juros
        
    def add_juros(self):
        juros = self.saldo * self.taxa_juros
        self.depositar(juros)

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, numero_conta, saldo):
        super().__init__(titular, saldo)