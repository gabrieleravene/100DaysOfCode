# sistema bancário básico - poo

class ContaBancaria:
    def __init__(self, titular, numero_conta,  saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"{self.titular} depositou R${valor}. O valor atual do saldo é: {self.saldo}.")
        
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"{self.titular} sacou R${valor}. O valor atual do saldo é R${self.saldo}. ")
        else:
            print("Saldo insuficiente")
            

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
        

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, numero_conta, saldo, taxa_juros):
        super().__init__(titular, numero_conta, saldo)
        self.taxa_juros = taxa_juros
        
    def add_juros(self):
        juros = self.saldo * self.taxa_juros
        self.depositar(juros)
        
        
conta_1 = ContaBancaria("Ana Silva", "123456", 1000)
conta_1.depositar(500)
conta_1.sacar(50)
print()
        
conta_p = ContaPoupanca("Ana Silva", "7891011", 2000, 0.05)
conta_p.depositar(1000)
conta_p.add_juros()
conta_p.sacar(500)
conta_p.sacar(100)

print()