from Viagem import Viagem


class ViagemControlador:
    def __init__(self):
        self.__viagens = dict()

    def cadastrarViagem(self, codigo_viagem, destino, origem, distancia, motorista_cpf, placa):
        if codigo_viagem in self.__viagens:
            print("\n\nCódigo/Viagem já cadastrado!")
            return False
        else:
            nova_viagem = Viagem(codigo_viagem, destino, origem,
                                 distancia, motorista_cpf, placa)
            self.__viagens[nova_viagem.getCodigo()] = nova_viagem
            return True

    def alterarViagem(self, codigo_viagem, destino, origem, distancia, motorista_cpf, placa):
        if codigo_viagem in self.__viagens:
            self.__viagens[codigo_viagem].setDestino(destino)
            self.__viagens[codigo_viagem].setOrigem(origem)
            self.__viagens[codigo_viagem].setDistancia(distancia)
            self.__viagens[codigo_viagem].setMotoristaCpf(motorista_cpf)
            self.__viagens[codigo_viagem].setPlaca(placa)
            return self.__viagens[codigo_viagem]
        else:
            return None

    def buscarViagem(self, codigo_viagem):
        if codigo_viagem in self.__viagens:
            return self.__viagens[codigo_viagem]
        else:
            return None
