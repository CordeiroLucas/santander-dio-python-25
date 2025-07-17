# Herança Simples em Python
# Demonstração de herança simples com sobrescrita de métodos

class Raiz:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"Raiz: {self.valor}"
    
    def funcao(self):
        return f"Função da Raiz: {self.valor}"
    
class Filho1(Raiz):
    def __init__(self, valor, valor_filho):
        super().__init__(valor)
        self.valor_filho = valor_filho

    def __str__(self):
        return f"Filho1: {self.valor} - {self.valor_filho}"

    # Sobrescrevendo a função da classe Raiz
    def funcao(self):
        return f"Função do Filho1: {self.valor_filho}"
    
class Filho2(Raiz):
    def __init__(self, valor, valor_filho):
        super().__init__(valor)
        self.valor_filho = valor_filho

    def __str__(self):
        return f"Filho2: {self.valor} - {self.valor_filho}"

    # Sobrescrevendo a função da classe Raiz
    def funcao(self):
        return f"Função do Filho2: {self.valor_filho}"
    
# Exemplo de uso

print('\nHerança Simples em Python\n')

raiz = Raiz(10)
filho1 = Filho1(20, 30)
filho2 = Filho2(40, 50)

print(raiz)
print(filho1)
print(filho2)

print(raiz.funcao())
print(filho1.funcao())
print(filho2.funcao())

# Herança Múltipla em Python
# Demonstração de herança múltipla com classes base e classe filha
# A herança múltipla permite que uma classe herde de várias classes base

# Torna-se necessário utilizar **kwargs para passar argumentos para as classes base
# Isso permite que a classe Filho receba argumentos adicionais e os repasse para as classes base

class Base1:
    def __init__(self, **kw):
        self.valor = kw['valor'] if 'valor' in kw else 0

    def funcao_base1(self):
        return f"Função Base1: {self.valor+100}"

class Base2:
    def __init__(self, **kw):
        self.valor = kw['valor'] if 'valor' in kw else -1

    def funcao_base2(self):
        return f"Função Base2: {self.valor-100}"

class Filho(Base1, Base2):
    def __init__(self, valor_filho, **kw):
        Base1.__init__(self, **kw)
        Base2.__init__(self, **kw)
        self.valor_filho = valor_filho

    def funcao_filho(self):
        return f"Função Filho: {self.valor} - {self.valor_filho}"
    
# Exemplo de uso
base1 = Base1(valor=100)
base2 = Base2(valor=200)

print('\n\nHerança Múltipla em Python\n')

print("\nBase1 e Base2 sem herança múltipla:")

print(base1.funcao_base1())
print(base2.funcao_base2())

print("\nFilho com herança múltipla:")

filho = Filho(valor_filho=300, valor=400)
print(filho.funcao_base1())
print(filho.funcao_base2())
print(filho.funcao_filho())

# Desvantagem da herança múltipla:
#  - A ordem de resolução de métodos (MRO) pode ser complexa e levar a comportamentos inesperados
#  - Fora que a herança múltipla pode tornar o código mais difícil de entender e manter