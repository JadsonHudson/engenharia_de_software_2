class Abastecimento:
    __id_abastecimento = -1

    def __init__(self, data, quantidade_combustivel, custo, veiculo):
        self.__id_abastecimento += 1
        self.__data = data
        self.__quantidade_combustivel = quantidade_combustivel
        self.__custo = custo
        self.__veiculo = veiculo

    def setIdAbastecimento(self, id_abastecimento):
        self.__id_abastecimento = id_abastecimento

    def getIdAbastecimento(self):
        return self.__id_abastecimento

    def setData(self, data):
        self.__data = data

    def getData(self):
        return self.__data

    def setQuantidadeCombustivel(self, quantidade_combustivel):
        self.__quantidade_combustivel = quantidade_combustivel

    def getQuantidadeCombustivel(self):
        return self.__quantidade_combustivel

    def setCusto(self, custo):
        self.__custo = custo

    def getCusto(self):
        return self.__custo

    def setVeiculo(self, veiculo):
        self.__veiculo = veiculo

    def getVeiculo(self):
        return self.__veiculo
