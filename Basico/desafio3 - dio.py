from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco:str):
        self._endereco = endereco
        self._contas:list[Conta] = []

    def realizar_transacao(self, conta, transacao):
        if not isinstance(transacao, Transacao):
            raise TypeError("O objeto deve ser uma instância da classe Transacao.")
        if not isinstance(conta, Conta):
            raise TypeError("O objeto deve ser uma instância da classe Conta.")
        transacao.registrar(conta)
        print(f"Transação realizada na conta {conta._numero} com sucesso!")
        
    def adicionar_conta(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("O objeto deve ser uma instância da classe Conta.")
        self._contas.append(conta)
        
    def listar_contas(self):
        for conta in self._contas:
            print(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento:str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        if data_nascimento.count("-") < 2:
            raise ValueError("Digite a data de nascimento no formato certo! DD-MM-YYYY")
        if not self._cpf:
            raise ValueError("CPF é obrigatório para Pessoa Física.")
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        dia_nasc, mes_nasc, ano_nasc = self._data_nascimento.split('-')
        return datetime.now().year - int(ano_nasc)
    
    def realizar_transacao(self, conta, transacao):
        if not isinstance(transacao, Transacao):
            raise TypeError("O objeto deve ser uma instância da classe Transacao.")
        if not isinstance(conta, Conta):
            raise TypeError("O objeto deve ser uma instância da classe Conta.")
        
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("O objeto deve ser uma instância da classe Conta.")
        self._contas.append(conta)

    def __str__(self):
        return f"Pessoa Física: {self._nome}, CPF: {self._cpf}, Data de Nascimento: {self._data_nascimento}"
 
class Conta:
    def __init__(self, numero, agencia, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()
        if not self._numero or not self._agencia:
            raise ValueError("Número e agência são obrigatórios para a conta.")

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero=numero, cliente=cliente)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_valor = valor > saldo
        
        if excedeu_valor:
            raise ValueError("Saldo insuficiente.")
        if valor < 0:
            raise ValueError("Valor de saque deve ser positivo.")
        
        self._saldo -= valor
        self._historico.adicionar_transacao(Saque(valor))
        return True

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("Valor de depósito deve ser positivo.")
        
        self._saldo += valor
        self._historico.adicionar_transacao(Deposito(valor))
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, agencia, limite=500, limite_saques=3):
        super().__init__(numero, agencia, cliente)
        self._limite:float = limite
        self._limite_saques:int = limite_saques
    
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self._historico.transacoes if transacao['tipo'] == Saque.__name__])
        if numero_saques >= self._limite_saques:
            raise ValueError("Limite de saques atingido.")
        if valor > self._limite:
            raise ValueError("Valor de saque excede o limite.")

        return super().sacar(valor)
    
    def __str__(self):
        return f"""
    Agência:\t{super().agencia}
    C/C:\t\t{self.numero}
    Titular:\t{self.cliente.nome}
    """      

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now(),
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
class Deposito(Transacao):
    def __init__(self, valor:float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

pessoa1 = PessoaFisica("Rua pedro paulo", 1234, "Luiz", "25-08-2002")
pessoa2 = PessoaFisica("Rua pedro Hnerique", 3456, "Pedro", "17-07-2015")

print(pessoa1.idade)
print(pessoa2.idade)

conta1 = ContaCorrente(1111, pessoa1, 1)
conta2 = ContaCorrente(2222, pessoa1, 2)
conta3 = ContaCorrente(3333, pessoa2, 3)

pessoa1.adicionar_conta(conta1)
pessoa1.adicionar_conta(conta2)

pessoa2.adicionar_conta(conta3)

print(pessoa2._contas[0].depositar(200))
print(pessoa2._contas[0].saldo)

print(pessoa1._contas[0].depositar(400))
print(pessoa1._contas[0].saldo)
print(pessoa1._contas[0].sacar(200))
print(pessoa1._contas[0].saldo)

print(pessoa1._contas[0].sacar(500))
print(pessoa1._contas[0].saldo)
