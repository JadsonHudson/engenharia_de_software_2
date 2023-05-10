from MotoristaControlador import MotoristaControlador
from VeiculoControlador import VeiculoControlador
from ViagemControlador import ViagemControlador
motoristaControlador = MotoristaControlador()
veiculoControlador = VeiculoControlador()
viagemControlador = ViagemControlador()


def gerenciar_motoristas():
    while True:
        print("\n\n\n========== GERENCIAR MOTORISTAS ==========")
        print("1. Cadastrar Motorista")
        print("2. Editar Motorista")
        print("3. Pesquisar Motorista")
        print("4. Deletar Motorista")
        print("0. Voltar\n\n")
        opcao = int(input("Escolha uma opção: "))

        match(opcao):
            case 1:
                print("\n\n\n========== CADASTRAR MOTORISTA ==========")
                nome = input("Nome do motorista: ")
                cpf = input("CPF do motorista: ")
                rg = input("RG do motorista: ")
                cnh = input("CNH do motorista: ")
                motoristaControlador.cadastrar(nome, cpf, rg, cnh)
            case 2:
                print("\n\n\n========== EDITAR MOTORISTA ==========")
                cpf = input("CPF do motorista: ")
                motorista = motoristaControlador.buscar(cpf)
                if motorista:
                    nome = input("Nome do motorista: ")
                    rg = input("RG do motorista: ")
                    cnh = input("CNH do motorista: ")
                    motoristaControlador.alterar(nome, cpf, rg, cnh)
                else:
                    print("Motorista não encontrado!")
            case 3:
                print("\n\n\n========== PESQUISAR MOTORISTA ==========")
                cpf = input("CPF do motorista: ")
                motorista = motoristaControlador.buscar(cpf)
                if motorista:
                    print("Nome: ", motorista.getNome())
                    print("CPF: ", motorista.getCpf())
                    print("RG: ", motorista.getRg())
                    print("CNH: ", motorista.getCnh())
                else:
                    print("Motorista não encontrado!")
            case 4:
                print("\n\n\n========== DELETAR MOTORISTA ==========")
                cpf = input("CPF do motorista: ")
                motoristaControlador.deletar(cpf)
            case 0:
                print("Voltando ao menu principal...")
                break


def gerenciar_veiculos():
    while True:
        print("\n\n\n========== GERENCIAR VEICULOS ==========")
        print("1. Cadastrar Veiculo")
        print("2. Editar Veiculo")
        print("3. Pesquisar Veiculo")
        print("4. Deletar Veiculo")
        print("5. Ver quilometragem de um veículo")
        print("0. Voltar\n\n")
        opcao = int(input("Escolha uma opção: "))

        match(opcao):
            case 1:
                print("\n\n\n========== CADASTRAR VEICULO ==========")
                marca = input("Marca do veículo: ")
                modelo = input("Modelo do veículo: ")
                ano = input("Ano do veículo: ")
                placa = input("Placa do veículo: ")
                numero_chassi = input("Número do chassi do veículo: ")
                cor = input("Cor do veículo: ")
                quilometragem = input("Quilometragem do veículo: ")
                veiculoControlador.cadastrar(marca, modelo, ano, placa,
                                             numero_chassi, cor, quilometragem)

            case 2:
                print("\n\n\n========== EDITAR VEICULO ==========")

                placa = input("Digite o placa do veículo a ser editado: ")
                if not veiculoControlador.buscar(placa):
                    print("Placa inválida!")
                else:
                    marca = input("Nova marca do veículo: ")
                    modelo = input("Novo modelo do veículo: ")
                    ano = input("Novo ano do veículo: ")
                    numero_chassi = input(
                        "Novo número do chassi do veículo: ")
                    cor = input("Nova cor do veículo: ")
                    quilometragem = input(
                        "Nova quilometragem do veículo: ")
                    veiculoControlador.alterar(
                        marca, modelo, ano, placa, numero_chassi, cor, quilometragem)

            case 3:
                print("\n\n\n========== PESQUISAR VEICULO ==========")

                placa = input("Digite a placa do veículo a ser pesquisado: ")
                if not veiculoControlador.buscar(placa):
                    print("Placa inválida!")
                else:
                    veiculo = veiculoControlador.buscar(placa)
                    print("\n\nMarca: ",   veiculo.getMarca())
                    print("Modelo: ",  veiculo.getModelo())
                    print("Ano: ", veiculo.getAno())
                    print("Placa: ",   veiculo.getPlaca())
                    print("Número do chassi: ",
                          veiculo.getNumeroChassi())
                    print("Cor: ", veiculo.getCor())
                    print("Quilometragem: ",
                          veiculo.getQuilometragem())
            case 4:
                print("\n\n\n========== DELETAR VEICULO ==========")

                placa = input("Digite a placa do veículo a ser deletado: ")
                if not veiculoControlador.buscar(placa):
                    print("Placa inválida!")
                else:
                    veiculoControlador.deletar(placa)
            case 5:
                print("\n\n\n========== VER QUILOMETRAGEM DE UM VEICULO ==========")

                placa = input("Digite a placa do veículo a ser pesquisado: ")
                if not veiculoControlador.buscar(placa):
                    print("Placa inválida!")
                else:
                    print("Quilometragem: ",
                          veiculoControlador.buscar(placa).getQuilometragem())
            case 0:
                print("Voltando ao menu principal...")
                break


def gerenciar_viagens():
    while True:
        print("\n\n\n========== GERENCIAR VIAGENS ==========")
        print("1. Cadastrar Viagem")
        print("2. Alterar Viagem")
        print("3. Pesquisar Viagem")
        print("4. Deletar Viagem")
        print("0. Voltar\n\n")
        opcao = int(input("Escolha uma opção: "))

        match(opcao):
            case 1:
                print("\n\n\n========== CADASTRAR VIAGEM ==========")
                codigo_viagem = input("Código da viagem: ")
                destino = input("Destino da viagem: ")
                origem = input("Origem da viagem: ")
                distancia = input("Distância da viagem: ")
                motorista_cpf = input("CPF do motorista: ")
                placa = input("Placa do veículo: ")

                viagemControlador.cadastrarViagem(
                    codigo_viagem, destino, origem, distancia, motorista_cpf, placa)

            case 2:
                print("\n\n\n========== ALTERAR VIAGEM ==========")

                codigo_viagem = input(
                    "Digite o código da viagem a ser editada: ")
                if not viagemControlador.buscarViagem(codigo_viagem):
                    print("\n\nCódigo inválido!")
                else:
                    destino = input("Novo destino da viagem: ")
                    origem = input("Nova origem da viagem: ")
                    distancia = input("Nova distancia da viagem: ")
                    motorista_cpf = input("Novo CPF do motorista: ")
                    placa = input("Nova placa do veículo: ")
                    sucess_full = viagemControlador.alterarViagem(
                        codigo_viagem, destino, origem, distancia, motorista_cpf, placa)
                    if sucess_full:
                        veiculoControlador.alterarQuilometragem(
                            placa, distancia)
                        motoristaControlador.adicionarViagem(
                            motorista_cpf, distancia)

            case 3:
                print("\n\n\n========== PESQUISAR VIAGEM ==========")

                codigo_viagem = input(
                    "Digite o código da viagem a ser pesquisada: ")
                if not viagemControlador.buscarViagem(codigo_viagem):
                    print("Código inválido!")
                else:
                    viagem = viagemControlador.buscarViagem(codigo_viagem)
                    print("\n\nCódigo da viagem: ", viagem.getCodigo())
                    print("Destino: ", viagem.getDestino())
                    print("Origem: ", viagem.getOrigem())
                    print("Distância: ", viagem.getDistancia())
                    print("CPF do motorista: ", viagem.getMotoristaCpf())
                    print("Placa do veículo: ", viagem.getPlaca())
            case 0:
                print("Voltando ao menu principal...")
                break


def main():
    while True:
        print("\n\n\n========== MENU ==========")
        print("1. Gerenciar Motoristas")
        print("2. Gerenciar Veiculos")
        print("3. Gerenciar Viagens")
        print("4. Registrar Abastecimento")
        print("5. Registrar Manutenção")
        print("6. Relatórios")
        print("0. Sair\n\n")

        opcao = int(input("Escolha uma opção: "))

        match(opcao):
            case 1:
                gerenciar_motoristas()
            case 2:
                gerenciar_veiculos()
            case 3:
                gerenciar_viagens()
                pass
            case 4:
                # registrar_abastecimento()
                pass
            case 5:
                # registrar_manutencao()
                pass
            case 6:
                # relatorios()
                pass
            case 0:
                print("Saindo do programa...")
                break


main()
# if opcao == "1":
#     marca = input("Marca do veículo: ")
#     modelo = input("Modelo do veículo: ")
#     ano = input("Ano do veículo: ")
#     veiculo = Veiculo(marca, modelo, ano)
#     veiculos.append(veiculo)
#     print("Veículo cadastrado com sucesso!")

# elif opcao == "2":
#     nome = input("Nome do motorista: ")
#     idade = input("Idade do motorista: ")
#     cpf = input("CPF do motorista: ")
#     motorista = Motorista(nome, idade, cpf)
#     motoristas.append(motorista)
#     print("Motorista cadastrado com sucesso!")

# elif opcao == "3":
#     if not veiculos:
#         print("Não há veículos cadastrados.")
#     else:
#         indice = int(input("Digite o índice do veículo a ser editado: "))
#         if indice >= len(veiculos) or indice < 0:
#             print("Índice inválido!")
#         else:
#             marca = input("Nova marca do veículo: ")
#             modelo = input("Novo modelo do veículo: ")
#             ano = input("Novo ano do veículo: ")
#             veiculos[indice].marca = marca
#             veiculos[indice].modelo = modelo
#             veiculos[indice].ano = ano
#             print("Veículo editado com sucesso!")

# elif opcao == "4":
#     if not motoristas:
#         print("Não há motoristas cadastrados.")
#     else:
#         indice = int(input("Digite o índice do motorista a ser editado: "))
#         if indice >= len(motoristas) or indice < 0:
#             print("Índice inválido!")
#         else:
#             nome = input("Novo nome do motorista: ")
#             idade = input("Nova idade do motorista: ")
#             cpf = input("Novo CPF do motorista: ")
#             motoristas[indice].nome = nome
#             motoristas[indice].idade = idade
#             motoristas[indice].cpf = cpf
#             print("Motorista editado com sucesso!")

# elif opcao == "5":
#     if not veiculos:
#         print("Não há veículos cadastrados.")
#     else:
#         for i, veiculo in enumerate(veiculos):
#             print(
#                 f"Índice: {i}, Marca: {veiculo.marca}, Modelo: {veiculo.modelo}, Ano: {veiculo.ano}")

# elif opcao == "6":
#     if not motoristas:
#         print("Não há motoristas cadastrados.")
#     else:
#         for i, motorista in enumerate(motoristas):
#             print(
#                 f"Índice: {i}, Nome: {motorista.nome}, Idade: {motorista.idade}, CPF: {motorista.cpf}")

# elif opcao == "7":
#     if not veiculos:
#         print("Não há veículos cadastrados.")
#     else:
#         indice = int(input("Digite o índice do veículo a ser deletado: "))
#         if indice >= len(veiculos) or indice < 0:
#             print("Índice inválido!")
#         else:
#             del veiculos[indice]
#             print("Veículo deletado com sucesso!")

# elif opcao == "8":
#     if not motoristas:
#         print("Não há motoristas cadastrados.")
#     else:
#         indice = int(
#             input("Digite o índice do motorista a ser deletado: "))
#         if indice >= len(motoristas) or indice < 0:
#             print("Índice inválido!")
#         else:
#             del motoristas[indice]
#             print("Motorista deletado com sucesso!")

# elif opcao == "0":
#     print("Saindo do programa...")
#     break

# else:
#     print("Opção inválida!")
