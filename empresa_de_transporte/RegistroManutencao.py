class RegistroManutencao:
    def __init__(self, codigo_manutencao, data, descricao, custo, placa):
        self.codigo_manutencao = codigo_manutencao
        self.data = data
        self.descricao = descricao
        self.custo = custo
        self.placa = placa

    def __str__(self):
        return f"ID: {self.codigo_manutencao}\nData: {self.data}\nDescrição: {self.descricao}\nID Veículo: {self.placa}\n"

    def __repr__(self):
        return self.__str__()

    def setCodigoManutencao(self, codigo_manutencao):
        self.codigo_manutencao = codigo_manutencao

    def getCodigoManutencao(self):
        return self.codigo_manutencao

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao

    def setCusto(self, custo):
        self.custo = custo

    def getCusto(self):
        return self.custo

    def setPlaca(self, placa):
        self.placa = placa

    def getPlaca(self):
        return self.placa
