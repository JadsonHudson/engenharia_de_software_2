class Veiculo:
    def __init__(self, marca, modelo, ano, placa, numero_chassi, cor, quilometragem):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__placa = placa
        self.__numero_chassi = numero_chassi
        self.__cor = cor
        self.__quilometragem = quilometragem

    def aumentarQuilometragem(self, distancia):
        self.__quilometragem += distancia

    def setMarca(self, marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo

    def setAno(self, ano):
        self.__ano = ano

    def getAno(self):
        return self.__ano

    def setPlaca(self, placa):
        self.__placa = placa

    def getPlaca(self):
        return self.__placa

    def setNumeroChassi(self, numero_chassi):
        self.__numero_chassi = numero_chassi

    def getNumeroChassi(self):
        return self.__numero_chassi

    def setCor(self, cor):
        self.__cor = cor

    def getCor(self):
        return self.__cor

    def setQuilometragem(self, quilometragem):
        self.__quilometragem = quilometragem

    def getQuilometragem(self):
        return self.__quilometragem
