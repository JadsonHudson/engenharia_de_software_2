class Viagem:
    def __init__(self, codigo_viagem, destino, origem, distancia, motorista_cpf, placa) -> None:
        self.__codigo_viagem = codigo_viagem
        self.__destino = destino
        self.__origem = origem
        self.__distancia = distancia
        self.__motorista_cpf = motorista_cpf
        self.__placa = placa

    def setCodigo(self, codigo_viagem):
        self.__codigo_viagem = codigo_viagem

    def getCodigo(self):
        return self.__codigo_viagem

    def setDestino(self, destino):
        self.__destino = destino

    def getDestino(self):
        return self.__destino

    def setOrigem(self, origem):
        self.__origem = origem

    def getOrigem(self):
        return self.__origem

    def setDistancia(self, distancia):
        self.__distancia = distancia

    def getDistancia(self):
        return self.__distancia

    def setMotoristaCpf(self, motorista_cpf):
        self.__motorista_cpf = motorista_cpf

    def getMotoristaCpf(self):
        return self.__motorista_cpf

    def setPlaca(self, placa):
        self.__placa = placa

    def getPlaca(self):
        return self.__placa
