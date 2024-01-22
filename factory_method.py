from abc import ABC, abstractmethod

# Produto - Abstrato
class Cafe(ABC):
    @abstractmethod
    def preparar(self) -> None: pass



# Produto Concreto
class CafeNormal(Cafe):
    def preparar(self) -> None:
        print('Café normal preparado')



# Produto Concreto
class CafeDescafeinado(Cafe):
    def preparar(self) -> None:
        print('Café descafeinado preparado')



# Criador - Abstrato
class CafeFactory(ABC):
    def __init__(self, tipo):
        self.cafe = self.get_cafe(tipo)
    
    # Método de fábrica - Abstrato
    @staticmethod
    @abstractmethod
    def get_cafe(tipo: str) -> Cafe: pass

    # Concretizado o produto, preparamos o café.
    def preparar_cafe(self):
        self.cafe.preparar()


# Criador concreto
class CafeNormalFactory(CafeFactory):
    @staticmethod
    def get_cafe(tipo: str) -> Cafe:
        match tipo:
            case 'N':
                return CafeNormal()
            case _:
                assert 0, 'Não temos café deste tipo.'



# Criador concreto
class CafeDescafeinadoFactory(CafeFactory):
    @staticmethod
    def get_cafe(tipo: str) -> Cafe:
        match tipo:
            case 'D':
                return CafeDescafeinado()
            case _:
                assert 0, 'Não temos café deste tipo.'



if __name__ == '__main__':
    from random import choice
    tipos = ['N', 'D']

    cafe1 = CafeNormalFactory(choice(tipos))
    cafe1.preparar_cafe()

    cafe2 = CafeDescafeinadoFactory(choice(tipos))
    cafe2.preparar_cafe()