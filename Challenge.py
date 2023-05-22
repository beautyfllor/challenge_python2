def cadastrar_cliente():
    print("Vamos realizar seu cadastro :)")
    print("Para isso, precisamos do seu nome, email e CPF.")
    print("Também é necessário que você crie uma senha e ela deve ter no mínimo 8 caracteres.")
    print("")

    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    cpf = input("Digite seu CPF: ")
    senha = input("Crie uma senha: ")
    while len(senha) < 8:
        print("")
        print("A senha deve conter no mínimo 8 caracteres!!")
        print("")
        senha = input("Crie uma senha: ")
    print("")
    
    print("Cadastro concluído com sucesso!!")
    print("Nome:", nome + "\nEmail:", email + "\nCPF:", cpf + "\nSenha:", senha)
    print("")

def cadastrar_bicicleta():
    print("Vamos realizar o cadastro da sua bicicleta :)")
    print("Para isso, precisamos da marca, modelo, número de série e do valor de sua bicicleta.")
    print("")

    marca = input("Digite a marca da bicicleta: ")
    modelo = input("Digite o modelo da  bicicleta: ")
    numeroSerie = input("Digite o número de série da bicicleta: ")
    valor = float(input("Digite o valor da bicicleta: "))
    print("")

    print("Cadastro concluído com sucesso!!")
    print("Marca:", marca + "\nModelo:", modelo + "\nNúmero de Série:", numeroSerie + "\nValor:", valor)
    print("")

def cadastrar_empresa_fabricante():
    print("Vamos realizar o cadastro da empresa fabricante de sua bicicleta :)")
    print("Para isso, precisamos do nome, CNPJ e site da empresa.")
    print("")

    nome = input("Digite o nome da empresa: ")
    cnpj = input("Digite o CNPJ da  empresa: ")
    site = input("Digite o site da empresa: ")
    print("")

    print("Cadastro concluído com sucesso!!")
    print("Nome:", nome + "\nCNPJ:", cnpj + "\nSite:", site)
    print("")

def cadastrar_pneu():
    print("Vamos realizar o cadastro dos penus de sua bicicleta :)")
    print("Para isso, precisamos do tamanho do aro, tempo de uso em anos e do valor dos pneus.")
    print("")

    aro = input("Digite o tamanho do aro: ")
    tempo_uso = input("Digite o tempo de uso dos pneus (em anos): ")
    valor = float(input("Digite o valor do pneu: "))
    print("")

    print("Cadastro concluído com sucesso!!")
    print("Tamanho do aro:", aro + "\nTempo de uso:", tempo_uso + "\nValor:", valor)
    print("")

def cadastrar_pedal():
    print("Vamos realizar o cadastro dos pedais de sua bicicleta :)")
    print("Para isso, precisamos da marca e do valor dos pedais.")
    print("")

    marca = input("Digite a marca do pedal: ")
    valor = float(input("Digite o valor do pedal: "))
    print("")
    
    print("Cadastro concluído com sucesso!!")
    print("Marca:", marca + "\nValor:", valor)
    print("")

def cadastrar_foto():
    print("Vamos realizar o cadastro da foto da bicicleta :)")
    print("Para isso, precisamos apenas de uma foto da sua bicicleta.")
    print("Ex: foto.png")
    print("")

    foto = input("Insira a foto: ")
    print("")
    
    print("Cadastro concluído com sucesso!!")
    print("Foto:", foto)
    print("")

def cadastrar_documentos():
    print("Vamos realizar o cadastro dos documentos da bicicleta :)")
    print("Para isso, precisamos da nota fiscal e do boleto.")
    print("")

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
    print("Vamos realizar o cadastro dos acessórios de sua bicicleta :)")
    print("Para isso, precisamos da descrição e do valor do acessório.")
    print("")

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