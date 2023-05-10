class Manutencao:
    __id_manutencao = -1

    def __init__(self, data, tipo_manutencao, custo, veiculo):
        self.__id_manutencao += 1
        self.__tipo_manutencao = tipo_manutencao
        self.__data = data
        self.__custo = custo
        self.__veiculo = veiculo

    def setIdManutencao(self, id_manutencao):
        self.__id_manutencao = id_manutencao

    def getIdManutencao(self):
        return self.__id_manutencao

    def setDescricao(self, tipo_manutencao):
        self.__tipo_manutencao = tipo_manutencao

    def getDescricao(self):
        return self.__tipo_manutencao

    def setData(self, data):
        self.__data = data

    def getData(self):
        return self.__data

    def setCusto(self, custo):
        self.__custo = custo

    def getCusto(self):
        return self.__custo

    def setVeiculo(self, veiculo):
        self.__veiculo = veiculo

    def getVeiculo(self):
        return self.__veiculo
