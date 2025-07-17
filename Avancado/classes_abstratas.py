from abc import ABC, abstractmethod

# A classe ControleRemoto é uma classe abstrata que define a interface para controle remoto de dispositivos.
# A classe ControleTV implementa essa interface para controlar uma TV.
class ControleRemoto(ABC): 
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    # Propriedade abstrata marca que deve ser implementada por subclasses
    @property
    @abstractmethod
    def marca(self):
        pass

# A interface torna obrigatória a implementação dos métodos ligar e desligar para qualquer classe que herde de ControleRemoto.

class ControleTV(ControleRemoto):
    def ligar(self):
        print("TV ligada")

    def desligar(self):
        print("TV desligada")
        
    @property
    def marca(self):
        return "Samsung"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ar condicionado ligado")

    def desligar(self):
        print("Ar condicionado desligado")
        
    @property
    def marca(self):
        return "LG"

controle = ControleTV()

controle.ligar()  # Método ligar da classe ControleRemoto
controle.desligar()  # Método desligar da classe ControleRemoto
print(controle.marca)

controle_ac = ControleArCondicionado()

controle_ac.ligar()  # Método ligar da classe ControleRemoto
controle_ac.desligar()  # Método desligar da classe ControleRemoto
print(controle_ac.marca)  # Propriedade marca da classe ControleArCondicionado
