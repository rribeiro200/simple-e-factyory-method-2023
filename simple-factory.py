from abc import ABC, abstractmethod

# Classe abstrata
class Cafe(ABC):
    @abstractmethod
    def preparar(self):
        pass



class CafeNormal(Cafe):
    # Sobescrevendo o método abstrato de Café
    def preparar(self):
        return 'Café normal preparado'



class CafeDescafeinado(Cafe):
    def preparar(self):
        return 'Café descafeinado preparado'



# Simple Factory - Vai fabricar o café, com base no tipo dele
class CafeFactory:
    @staticmethod
    def criar_cafe(tipo):
        match tipo:
            case 'N':
                return CafeNormal()
            case 'D':
                return CafeDescafeinado()
            case _:
                assert 0, 'Não temos esse tipo de café aqui'



# Executar / Usar a Simple Factory
if __name__ == '__main__':
    tipo_cafe = input("Digite o tipo do café (normal ou descafeinado): ")

    fazer_cafe = CafeFactory.criar_cafe(tipo_cafe)

    print(fazer_cafe.preparar())