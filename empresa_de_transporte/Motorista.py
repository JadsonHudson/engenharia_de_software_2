class Motorista:
    def __init__(self, nome: str, cpf: str, rg: str, cnh: str, distancia_percorrida: float = 0.0, quantidade_viagens: int = 0):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__cnh = cnh
        self.__distancia_percorrida = distancia_percorrida
        self.__quantidade_viagens = quantidade_viagens
        # self.__data_nascimento = data_nascimento
        # self.__endereco = endereco
        # self.__telefone = telefone
        # self.__email = email
        # self.__senha = senha

    def aumentarQuantidadeViagens(self):
        self.__quantidade_viagens += 1

    def aumentarDistanciaPercorrida(self, distancia):
        self.__distancia_percorrida += distancia

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self) -> str:
        return self.__cpf

    def setRg(self, rg):
        self.__rg = rg

    def getRg(self):
        return self.__rg

    def setCnh(self, cnh):
        self.__cnh = cnh

    def getCnh(self):
        return self.__cnh

    def setQuantidadeViagens(self, quantidade_viagens):
        self.__quantidade_viagens = quantidade_viagens

    def getQuantidadeViagens(self):
        return self.__quantidade_viagens

    def setDistanciaPercorrida(self, distancia_percorrida):
        self.__distancia_percorrida = distancia_percorrida

    def getDistanciaPercorrida(self):
        return self.__distancia_percorrida

    # def setDataNascimento(self, data_nascimento):
    #     self.__data_nascimento = data_nascimento

    # def getDataNascimento(self):
    #     return self.__data_nascimento

    # def setEndereco(self, endereco):
    #     self.__endereco = endereco

    # def getEndereco(self):
    #     return self.__endereco

    # def setTelefone(self, telefone):
    #     self.__telefone = telefone

    # def getTelefone(self):
    #     return self.__telefone

    # def setEmail(self, email):
    #     self.__email = email

    # def getEmail(self):
    #     return self.__email

    # def setSenha(self, senha):
    #     self.__senha = senha

    # def getSenha(self):
    #     return self.__senha
