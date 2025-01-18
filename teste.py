from clientes import Cliente
from contas import Conta
paulo = Cliente("Paulo da Costa", "364-2975")
teresa = Cliente("Teresa Nogueira", "342-8219")
conta1 = Conta([paulo], 1, 3000)
conta2 = Conta([teresa, paulo], 2, 1500)
conta1.saque(100)
conta2.deposito(500)
conta1.saque(140)
conta2.deposito(170)
conta2.saque(300)
conta1.extrato()
conta2.extrato()

