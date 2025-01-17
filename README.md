#Banco_lista

class Cliente:
  def __init__(self, nome, telefone):
    self.nome = nome
    self.telefone = telefone

class Conta:    
    def __init__(self, clientes, números, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)
    def resumo(self):
        print(f"CC Nº {self.número} saldo: {self.saldo:10.2f}")
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPOSITO", valor])
    def extrato(self):
        print(f"Extrato CC Nº {self.número}\n")
        for o in self.operações:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n  Saldo: {self.saldo:10.2f}\n")

class Banco:
    def __init__(self,nome):
        self.nome = nome
        self.clientes =[]
        self.contas =[] 
    def abre_conta(self,conta):
        self.contas.append(conta)
    def lista_contas(self):
        for c in self.contas:
            c.resumo()
