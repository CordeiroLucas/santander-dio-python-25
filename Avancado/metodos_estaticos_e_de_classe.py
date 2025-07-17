class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Método de classe constroi um objeto a partir do construtor
    # de classe, permitindo criar instâncias com base em outros dados.

    @classmethod
    def criar_apartir_data_nasc(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    # Método estático não depende de instância ou classe, é independente
    # e pode ser chamado sem criar uma instância da classe.

    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18
    
    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

p = Pessoa.criar_apartir_data_nasc(1990, 5, 15, 'Maria')

print(p)  # Saída: Maria, 30 anos

print(p.e_maior_de_idade(p.idade))  # Saída: True
print(p.e_maior_de_idade(16))  # Saída: False