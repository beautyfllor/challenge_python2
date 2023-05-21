def cadastrar_cliente():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    cpf = input("Digite seu CPF: ")
    senha = input("Crie uma senha: ")
    print("")
    
    print("Cadastro concluído com sucesso!!")
    print("Nome:", nome + "\nEmail:", email + "\nCPF:", cpf + "\nSenha:", senha)
    print("")

def cadastrar_bicicleta():
    marca = input("Digite a marca da bicicleta: ")
    modelo = input("Digite o modelo da  bicicleta: ")
    numeroSerie = input("Digite o número de série da bicicleta: ")
    valor = float(input("Digite o valor da bicicleta: "))
    print("")

    print("Cadastro concluído com sucesso!!")
    print("Marca:", marca + "\nModelo:", modelo + "\nNúmero de Série:", numeroSerie + "\nValor:", valor)
    print("")

def cadastrar_empresa_fabricante():
    nome = input("Digite o nome da empresa: ")
    cnpj = input("Digite o CNPJ da  empresa: ")
    site = input("Digite o site da empresa: ")
    print("")

    print("Cadastro concluído com sucesso!!")
    print("Nome:", nome + "\nCNPJ:", cnpj + "\nSite:", site)
    print("")

def cadastrar_pneu():
    aro = input("Digite o tamanho do aro: ")
    tempo_uso = input("Digite o tempo de uso dos pneus (em anos): ")
    valor = float(input("Digite o valor do pneu: "))
    print("")

    print("Cadastro concluído com sucesso!!")
    print("Tamanho do aro:", aro + "\nTempo de uso:", tempo_uso + "\nValor:", valor)
    print("")

def cadastrar_pedal():
    marca = input("Digite a marca do pedal: ")
    valor = float(input("Digite o valor do pedal: "))
    print("")
    
    print("Cadastro concluído com sucesso!!")
    print("Marca:", marca + "\nValor:", valor)
    print("")

def cadastrar_foto():
    foto = input("Insira a foto: ")
    print("")
    
    print("Cadastro concluído com sucesso!!")
    print("Foto:", foto)
    print("")

def cadastrar_documentos():
    documentos = []

    nota_fiscal = input("Insira a nota fiscal: ")
    documentos.append(nota_fiscal)
    boleto = input("Insira o boleto: ")
    documentos.append(boleto)
    print("")
    
    print("Cadastro concluído com sucesso!!")
    print("Nota Fiscal:", documentos[0] + "\nBoleto:", documentos[1])
    print("")

def cadastrar_acessorio():
    descricao = input("Escreva uma breve descrição do acessório: ")
    valor = float(input("Digite o valor do acessório: "))
    print("")
    
    print("Cadastro concluído com sucesso!!")
    print("Descrição:", descricao + "\nValor:", valor)
    print("")

def recebe_operacao():
    operacao = int(input("Qual operação deseja realizar? \n(1) Cadastrar Cliente \n(2) Cadastrar Bicicleta"
        + "\n(3) Cadastrar Empresa Fabricante  \n(4) Cadastrar Pneu \n(5) Cadastrar Pedal"
        + "\n(6) Cadastrar Foto \n(7) Cadastrar Documentos  \n(8) Cadastrar Acessorio"))
    print("")
    return operacao

def define_operacao(operacao):
    match operacao:
        case 1:
            cadastrar_cliente()
        case 2:
            cadastrar_bicicleta()
        case 3:
            cadastrar_empresa_fabricante()
        case 4:
            cadastrar_pneu()
        case 5:
            cadastrar_pedal()
        case 6:
            cadastrar_foto()
        case 7:
            cadastrar_documentos()
        case 8:
            cadastrar_acessorio()
        case _:
            print("Escolha incorreta!")

def main():
    print("")
    print("----- U.R.S.A - Unity of Resolutions for Softwares and Applications -----")
    print("")
    print("Seja bem-vindo(a) ao serviço de vistoria de bicicletas!")
    print("")

    continua = 1

    while continua == 1:
        operacao = recebe_operacao()
        define_operacao(operacao)

        continua = int(input("Deseja continuar? \n(1) Sim \n(2) Não"))
        print("")

    print("Muito Obrigada!")

main()