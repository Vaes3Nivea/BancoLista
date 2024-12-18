# BancoLista
class BancoLista:
    def __init__(self, nome, taxa_juros=0.01):
        self.nome = nome
        self.contas = []  # Lista para armazenar as contas
        self.taxa_juros = taxa_juros  # Taxa de juros para contas poupança

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta ao repositório.
        """
        self.contas.append(conta)

    def remover_conta(self, numero_conta):
        """
        Remove uma conta do repositório com base no número da conta.
        """
        self.contas = [conta for conta in self.contas if conta.numero != numero_conta]

    def buscar_conta_por_numero(self, numero_conta):
        """
        Retorna a conta correspondente ao número fornecido.
        """
        for conta in self.contas:
            if conta.numero == numero_conta:
                return conta
        return None

    def buscar_contas_por_cliente(self, nome_cliente):
        """
        Retorna uma lista de contas associadas ao nome de um cliente.
        """
        return [conta for conta in self.contas if conta.cliente.nome.lower() == nome_cliente.lower()]

    def listar_contas(self):
        """
        Exibe todas as contas no repositório.
        """
        for conta in self.contas:
            print(conta)

    def render_juros(self, numero_conta):
        """
        Rende juros para uma conta poupança com base na taxa de juros atual.
        """
        conta = self.buscar_conta_por_numero(numero_conta)
        if isinstance(conta, ContaPoupanca):
            conta.rende_juros(self.taxa_juros)
        else:
            print("A conta especificada não é uma conta poupança.")

# Classe Conta para exemplificar o funcionamento
class Conta:
    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor

    def __str__(self):
        return f"Conta {self.numero} | Cliente: {self.cliente.nome} | Saldo: R${self.saldo:.2f}"

# Classe ContaPoupanca para contas poupança
class ContaPoupanca(Conta):
    def rende_juros(self, taxa_juros):
        """
        Aplica os juros ao saldo da conta.
        """
        self.saldo += self.saldo * taxa_juros

# Classe Cliente para exemplificar o funcionamento
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

# Exemplo de uso
if __name__ == "__main__":
    banco = BancoLista("Banco Central", taxa_juros=0.02)

    cliente1 = Cliente("Paulo Aragão", "123.456.789-00")
    cliente2 = Cliente("Carlos Araújo", "987.654.321-00")

    conta1 = Conta(1, cliente1, 800)
    conta2 = ContaPoupanca(2, cliente2, 2000)
    conta3 = ContaPoupanca(3, cliente1, 500)

    banco.adicionar_conta(conta1)
    banco.adicionar_conta(conta2)
    banco.adicionar_conta(conta3)

    print("=== Todas as contas ===")
    banco.listar_contas()

    print("\n=== Render juros para conta poupança ===")
    banco.render_juros(2)
    banco.render_juros(3)

    print("\n=== Todas as contas após render juros ===")
    banco.listar_contas()

    print("\n=== Remover conta ===")
    banco.remover_conta(1)
    banco.listar_contas()
