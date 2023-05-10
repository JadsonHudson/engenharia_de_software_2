from Veiculo import Veiculo


class VeiculoControlador():
    def __init__(self):
        self.__veiculos = dict()

    def cadastrar(self, marca, modelo, ano, placa, numero_chassi, cor, quilometragem):
        if placa in self.__veiculos:
            print("\n\nVeiculo já cadastrado\n")
            return
        veiculo = Veiculo(marca, modelo, ano, placa,
                          numero_chassi, cor, quilometragem)
        self.__veiculos[placa] = veiculo

    def alterar(self, marca, modelo, ano, placa, numero_chassi, cor, quilometragem):
        veiculo = Veiculo(marca, modelo, ano, placa,
                          numero_chassi, cor, quilometragem)
        self.__veiculos[placa] = veiculo

    def alterarQuilometragem(self, placa, distancia):
        if placa in self.__veiculos:
            self.__veiculos[placa].aumentarQuilometragem(distancia)
            return self.__veiculos[placa]
        else:
            return None

    def buscar(self, placa):
        if placa in self.__veiculos:
            return self.__veiculos[placa]
        return None

    def deletar(self, placa):
        if placa in self.__veiculos:
            self.__veiculos.pop(placa)
            print("\n\nVeiculo removido com sucesso\n")
        else:
            print("\n\nVeiculo não encontrado\n")

    def listar(self):
        return self.__veiculoDAO.listar()

    def listar_por_motorista(self, cpf):
        return self.__veiculoDAO.listar_por_motorista(cpf)
