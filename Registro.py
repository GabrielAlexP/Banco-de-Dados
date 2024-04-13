import pickle
def registro(nome, idade, telefone, cpf, email):
    """
    :param nome: The parameter "nome" is for giving the name that the user desires and using it as a basis for research.
    :param idade:"Idade" is the information about the number of years of life that the user inputs.
    :param telefone:"Telefone" is the user's cell phone number.
    :param cpf:"CPF" is the provided CPF document.
    :param email:"Email" is for saving a contact form for the user.
    :return:This function will be used to create a dictionary and store the data inside.
    """

    try:
        with open('pessoas.pickle', 'rb') as file:
            pessoas = pickle.load(file)
    except FileNotFoundError:
        pessoas = {}
    pessoas[nome] = {
        'idade': idade,
        'telefone': telefone,
        'cpf': cpf,
        'email': email,
    }
    with open('pessoas.pickle', 'wb') as file:
        pickle.dump(pessoas, file)

def cadastro():
    """
    :return: The function "cadastro" will be used to show names when the user ask
    """
    with open('pessoas.pickle', 'rb') as file:
        pessoas = pickle.load(file)
    nomes = list(pessoas.keys())
    for nome in nomes:
        print(nome.center(60))

def novo():
    """
    :return:"novo" serves to register the information and pass it on to "registro".
    """
    while True:
        nome = input('Digite o nome: ')
        if not nome.isalpha():
            print('Por favor, digite apenas letras')
            continue

        idade = input('Digite a idade: ')
        if not idade.isdigit():
            print('Por favor, digite apenas números inteiros.')
            continue
        idade = int(idade)

        telefone = input('Digite o número de telefone: ')
        cpf = input('Digite o CPF: ')
        email = input('Digite o e-mail: ')

        registro(nome, idade, telefone, cpf, email)
        break
def menu():
    """
    :return:"menu" shows the user the options to choose the program's utility.
    """
    print(30*'-=')
    print('MENU PRINCIPAL'.center(60))
    print(30*'-=')
    print ('1-Ver Pessoas Cadastradas')
    print ('2-Novo Cadastro')
    print ('3-Pesquisar Por Pessoa')
    print ('4-Apagar uma Pessoa')
    print ('5-Excluir Banco de Dados')
    print ('6-Encerrar programa')
    print ('-='*30)
def pesquisa():
    """
    :return:It will show the user the information of the chosen name.
    """
    with open('pessoas.pickle', 'rb') as file:
        pessoas = pickle.load(file)
    nome_pesquisa = input('Digite o nome da pessoa que você deseja pesquisar: ').title().strip()
    if nome_pesquisa in pessoas:
        pessoa = pessoas[nome_pesquisa]
        print("Nome: {nome_pesquisa}")
        print(f"Idade: {pessoa['idade']}")
        print(f"Telefone: {pessoa['telefone']}")
        print(f"CPF: {pessoa['cpf']}")
        print(f"Email: {pessoa['email']}")
    else:
        print(f'{nome_pesquisa} não está cadastrado')
def apaga_tudo():
    """
    :return: Deletes all user information.
    """
    with open('pessoas.pickle', 'wb') as file:
        pickle.dump({}, file)
def apaga_um(nome):
    """
    :param nome: Specify the chosen one.
    :return: Dele all info to "nome"
    """
    with open('pessoas.pickle', 'rb') as file:
        pessoas = pickle.load(file)
    if nome in pessoas:
        del pessoas[nome]
        with open('pessoas.pickle', 'wb') as file:
            pickle.dump(pessoas, file)
        print(f'{nome} foi excluído do banco de dados.')
    else:
        print(f'{nome} não está cadastrado no banco de dados.')


def main():
    """
    :return: The main part of the code, where the "if" statements execute the option chosen by the user in the "menu".
    """
    while True:
        menu()
        while True:
            try:
                perg = int(input('Escolha uma opção: '))
                print(30*'-=')
                break
            except:
                print('Por favor, digite apenas números.')
        if perg == 1:
            cadastro()
        elif perg == 2:
            novo()
        elif perg == 3:
            pesquisa()
        elif perg == 4:
            nome = input('Digite o nome da pessoa a ser excluída: ').title().strip()
            apaga_um(nome)
        elif perg == 5:
            apaga_tudo()
            print('Banco de Dados apagado')
        elif perg == 6:
            print('Encerrando programa...')
            break
        else:
            print('Opção inválida, tente novamente.')
