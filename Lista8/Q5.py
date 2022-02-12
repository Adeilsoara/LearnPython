'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos:
número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome,
depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''
class ContaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self, novoNome):
        self.nomeCorrentista = novoNome

    def deposito(self, novoSaldo):
        self.saldo += novoSaldo
        return self.saldo

    def saque(self, novoSaldoSaque):
        self.saldo -= novoSaldoSaque
        return self.saldo

conta1 = ContaCorrente('000', 'Adeilson', 250)
print(conta1.__dict__)
conta1.alterarNome('Milena')
print(conta1.__dict__)

conta1.deposito(100)
print(conta1.__dict__)

conta1.saque(50)
print(conta1.__dict__)
