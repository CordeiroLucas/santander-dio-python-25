from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, **kw):
        self._nome = kw.get("nome")
        self._idade = kw.get("idade")
        self._cpf = kw.get("cpf")
        if not self._nome or not self._idade or not self._cpf:
            raise ValueError("Nome, idade e CPF são obrigatórios.")
        
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        # Simples validação de CPF (apenas para fins de exemplo)
        return len(cpf) == 11 and cpf.isdigit()

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_cpf(self):
        return self._cpf

    def __str__(self):
        return ", ".join(f"{k}: {v}" for k, v in self.__dict__.items())

class Cliente(Pessoa):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.conta = kw.get("conta")
        self.saldo = kw.get("saldo", 0.0)
        
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do depósito deve ser maior que zero.")
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor do saque deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para o saque.")
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        
    def __str__(self):
        return f"{super().__str__()}, Conta: {self.conta}, Saldo: R$ {self.saldo:.2f}"

class Banco:
    def __init__(self, **kw):
        self.nome = kw.get("nome")
        self.agencia = kw.get("agencia")
        self._clientes = []

    def __str__(self):
        return ', '.join(f"{k}: {v}" for k, v in self.__dict__.items())
    
    def gerar_numero_conta(self):
        import random
        conta_gerada = random.randint(1000, 9999)
        digito_verificador = random.randint(0, 9)
        
        if conta_gerada in [c.conta for c in self._clientes]:
            return self.gerar_numero_conta()
        return f"{conta_gerada}-{digito_verificador}"

    def cadastrar_cliente(self, pessoa):
        if not isinstance(pessoa, Pessoa):
            raise TypeError("A pessoa deve ser uma instância da classe Pessoa.")
        if not pessoa.validar_cpf(pessoa.get_cpf()):
            raise ValueError("CPF inválido.")
        if pessoa.get_cpf() in [c.get_cpf() for c in self._clientes]:
            raise ValueError("CPF já cadastrado.")

        cliente = Cliente(nome=pessoa.get_nome(), idade=pessoa.get_idade(), cpf=pessoa.get_cpf(), conta=self.gerar_numero_conta(), saldo=0.0)
        self._clientes.append(cliente)
        return cliente
    
    # Transferência entre clientes do Banco
    
    def transferir_mesmo_banco(self, cliente_origem, cliente_destino, valor):
        if cliente_origem not in self._clientes or cliente_destino not in self._clientes:
            raise ValueError("Cliente não encontrado.")
        if valor <= 0:
            raise ValueError("Valor da transferência deve ser maior que zero.")
        if cliente_origem.saldo < valor:
            raise ValueError("Saldo insuficiente para a transferência.")
        
        cliente_origem.sacar(valor)
        cliente_destino.depositar(valor)
        print(f"Transferência de R$ {valor:.2f} realizada com sucesso de {cliente_origem.get_nome()} para {cliente_destino.get_nome()}.")

    def transferir_diferente_banco(self, cliente_origem, cliente_destino, banco_destino, valor):
        if cliente_origem not in self._clientes:
            raise ValueError("Cliente de origem não encontrado.")
        if cliente_destino not in banco_destino.get_clientes():
            raise ValueError("Cliente de destino não encontrado no banco de destino.")
        if valor <= 0:
            raise ValueError("Valor da transferência deve ser maior que zero.")
        if cliente_origem.saldo < valor:
            raise ValueError("Saldo insuficiente para a transferência.")
        
        cliente_origem.sacar(valor)
        cliente_destino.depositar(valor)
        print(f"Transferência de R$ {valor:.2f} realizada com sucesso de {cliente_origem.get_nome()} para {cliente_destino.get_nome()} no banco {banco_destino.nome}.")

    def listar_clientes(self):
        if not self._clientes:
            return "Nenhum cliente cadastrado."
        return "\n".join(str(cliente) for cliente in self._clientes)

    def get_clientes(self):
        return self._clientes

# Exemplo de uso =========================================================================

pessoa1 = Pessoa(nome="João", idade=30, cpf="12345678901")
pessoa2 = Pessoa(nome="Maria", idade=25, cpf="10987654321")
pessoa3 = Pessoa(nome="Junio", idade=33, cpf="10987654321")


banco1 = Banco(nome="Santander1", agencia="001")

banco1.cadastrar_cliente(pessoa1)
banco1.cadastrar_cliente(pessoa2)

banco2 = Banco(nome="Santander2", agencia="002")


print(banco1.listar_clientes())  # Saída: Nome: João, Idade: 30
# print(banco2.listar_clientes()) 

