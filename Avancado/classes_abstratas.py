class Classe1:
    # Variáveis de classe
    variavel_classe = 0
    nome_classe = 'Classe1'
    
    def __init__(self, nome, valor):
        # Variaveis de instância
        self.nome = nome
        self.valor = valor
    
    def __str__(self):
        return f"{self.variavel_classe} {self.nome_classe}: {self.nome} - {self.valor}"


# Exemplo de uso

primeira_instancia = Classe1('Instância 1', 10)
segunda_instancia = Classe1('Instância 2', 20)

print(primeira_instancia)
print(segunda_instancia)

# Modificando variáveis de classe

Classe1.variavel_classe = 5
Classe1.nome_classe = 'NovaClasse Geral'

print(primeira_instancia)
print(segunda_instancia)

# Modificando variáveis de instância

primeira_instancia.variavel_classe = 3
primeira_instancia.nome_classe = 'NovaClasse1 Local'

print(primeira_instancia)
print(segunda_instancia)

# Modificando variáveis de classe novamente

Classe1.variavel_classe = 10
Classe1.nome_classe = 'Classe1'

print(primeira_instancia)
print(segunda_instancia)

# Variaveis de classe são compartilhadas entre todas as instâncias
# Mudanças em variáveis de instância não afetam outras instâncias
