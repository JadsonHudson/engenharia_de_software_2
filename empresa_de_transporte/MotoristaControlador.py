from Motorista import Motorista


class MotoristaControlador:
    def __init__(self):
        self.__motorista = dict()

    def cadastrar(self, nome, cpf, rg, cnh):
        if self.buscar(cpf):
            print("\n\nCPF já cadastrado!")
            return
        motorista = Motorista(nome, cpf, rg, cnh)
        self.__motorista[motorista.getCpf()] = motorista
        print(self.__motorista[f"{cpf}"].getNome())

    def adicionarViagem(self, cpf, distancia):
        if not self.buscar(cpf):
            print("\n\nCPF não cadastrado!")
            return
        self.__motorista[cpf].aumentarDistanciaPercorrida(distancia)
        self.__motorista[cpf].aumentarQuantidadeViagens()

    def buscar(self, cpf):
        if cpf in self.__motorista:
            return self.__motorista[cpf]
        else:
            return None

    def alterar(self, nome, cpf, rg, cnh):
        if not self.buscar(cpf):
            print("\n\nCPF não cadastrado!")
            return
        motorista = Motorista(nome, cpf, rg, cnh)
        self.__motorista[motorista.getCpf()] = motorista

    def deletar(self, cpf):
        if not self.buscar(cpf):
            print("\n\nCPF não cadastrado!")
            return
        self.__motorista.pop(cpf)
