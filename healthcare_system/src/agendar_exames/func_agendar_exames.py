import os
from healthcare_system.src.utils import *
import requests

def pega_cpf():
    cpf = input("CPF do paciente:")
    while len(cpf) != 11 or not cpf.isdigit() or not validar_cpf(cpf):
        print(f"{Cor.CINZA_CLARO}CPF inválido. Deve conter 11 dígitos numéricos e ser válido.{Cor.RESET}")
        cpf = input("CPF do paciente:")
    return cpf


def consultar_cep(cep):
    while True:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'erro' not in data:
                    endereco = {
                        'cep': data['cep'],
                        'logradouro': data['logradouro'],
                        'complemento': data['complemento'],
                        'bairro': data['bairro'],
                        'localidade': data['localidade'],
                        'uf': data['uf'],
                    }
                    return endereco
                else:
                    print("CEP não encontrado.")
                    cep = input("Digite o CEP novamente: ")
            else:
                print("Erro ao consultar o CEP.")
                cep = input("Digite o CEP novamente: ")
        except requests.RequestException as e:
            print("Erro de conexão:", e)
            cep = input("Digite o CEP novamente: ")


def pega_idade():
    idade = verifica_num(input("Idade do paciente:"), "Idade do paciente:",
                         f"{Cor.CINZA_CLARO}A idade deve ser cadastrada em números inteiros (1, 10, 55, 80 etc...){Cor.RESET}")
    return idade


def pega_data_nascimento():
    while True:
        data_nascimento = input("Data de nascimento do paciente (DD-MM-YYYY): ")
        if verifica_data(data_nascimento):
            data_nascimento_obj = datetime.strptime(data_nascimento, '%d-%m-%Y')
            data_atual = datetime.now()
            if data_nascimento_obj < data_atual:
                return data_nascimento
            else:
                print(
                    f"{Cor.CINZA_CLARO}Data de nascimento inválida. Deve ser anterior à data atual.{Cor.RESET}")
        else:
            print(
                f"{Cor.CINZA_CLARO}Data de nascimento inválida. Deve ser preenchida neste formato: DD-MM-YYYY{Cor.RESET}")


def pega_telefone():
    telefone = input("Telefone para contato do paciente. (Exemplo: (dd) xxxxx-xxxx): ")
    telefone_formatado = verifica_telefone(telefone)
    while telefone_formatado is None:
        telefone = input("Telefone para contato do paciente. (Exemplo: (dd) xxxxx-xxxx): ")
        telefone_formatado = verifica_telefone(telefone)
    return telefone_formatado


def pega_sexo():
    while True:
        opcao_sexo = input("Sexo do paciente [m/f]: ").strip().lower()
        if not opcao_sexo:
            print(f"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")
            continue
        sexo = escolher_opcao(opcao_sexo[0], ['m', 'f'], "Sexo do paciente: [m/f] ",
                              f"{Cor.CINZA_CLARO}Digite uma opção válida!{Cor.RESET}")
        return sexo


def pega_tipo_sanguineo():
    imprimir_tabela_tipos_sanguineos()
    lista_sangue = ["a-", "a+", "b+", "b-", "ab+", "ab-", "o+", "o-"]
    tipo_sanguineo = escolher_opcao_lista(input("Tipo Sanguíneo do paciente: "), lista_sangue,
                                          "Tipo Sanguíneo do paciente: ",
                                          f"{Cor.CINZA_CLARO}O tipo sanguíneo deve ser uma opção existente ex:{lista_sangue}{Cor.RESET}")
    return tipo_sanguineo


def pega_alergia():
    while True:
        try:
            opcao_alergia = input("O paciente tem alguma alergia? ").strip().lower()
            if not opcao_alergia:
                print(f"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")
                continue
            opcao_alergia = escolher_opcao(opcao_alergia[0], ["s", "n"], "O paciente tem alguma alergia?",
                                           f"{Cor.CINZA_CLARO}Digite uma resposta válida!{Cor.RESET}")
            if opcao_alergia == "s":
                alergia = input("Qual?")
            else:
                alergia = "não possui"

            return alergia
        except IndexError:
            print(f"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")


def pega_doenca_cronica():
    while True:
        try:
            opcao_saude_cronico = input("O paciente tem algum problema de saúde crônico? ").strip().lower()
            if not opcao_saude_cronico:
                print(F"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")
                continue
            opcao_saude_cronico = escolher_opcao(opcao_saude_cronico[0], ["s", "n"],
                                                 "O paciente tem algum problema de saúde crônico?",
                                                 f"{Cor.CINZA_CLARO}Digite uma resposta válida!{Cor.RESET}")
            if opcao_saude_cronico == "s":
                saude_cronico = input("Qual?")
            else:
                saude_cronico = "não possui"

            return saude_cronico
        except IndexError:
            print(F"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")


def pega_prioritario():
    lista_prioritario = ["pcd", "idoso", "gestante"]
    while True:
        try:
            opcao_prioridade = input("O paciente é prioritário? ").strip().lower()
            if not opcao_prioridade:
                print(f"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")
                continue
            opcao_prioridade = escolher_opcao(opcao_prioridade[0], ["s", "n"], "O paciente é prioritário?",
                                               f"{Cor.CINZA_CLARO}Digite uma resposta válida!{Cor.RESET}")
            if opcao_prioridade == "s":
                prioritario = escolher_opcao_lista(input(f"Qual das categorias ({', '.join(lista_prioritario)}): "),
                                                    lista_prioritario,
                                                    f"Qual das categorias ({', '.join(lista_prioritario)}):",
                                                    f'{Cor.CINZA_CLARO}A opção deve ser uma destas: {", ".join(lista_prioritario)}{Cor.RESET}')
            else:
                prioritario = "não prioritario"

            return prioritario
        except IndexError:
            print(f"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")


def pega_exame():
    lista_exames = ["raio-x", "ultrassom", "tomografia", "ressonancia", "ecocardiograma"]
    exame = escolher_opcao_lista(input(f"Exame que deseja realizar ({', '.join(lista_exames)}): "), lista_exames,
                                 f"Exame que deseja realizar ({', '.join(lista_exames)}):",
                                 f"{Cor.CINZA_CLARO}Escolha entre uma das opções apresentadas{Cor.RESET}")
    return exame


def pega_data_exame():
    while True:
        data_exame = input("Data para realização do exame DD-MM-YYYY:")
        if verifica_data_futura(data_exame):
            return data_exame
            break
        else:
            print(
                f"{Cor.CINZA_CLARO}Data inválida, deve ser preenchido neste formato: DD-MM-YYYY (dia-mês-ano).{Cor.RESET}")

def dict_append(chave, valor):
    ficha_paciente[chave] = valor


def imprimir_ficha_completa():
    print(f"{Cor.VERDE}𝙛𝙞𝙘𝙝𝙖 𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙖 𝙙𝙤 𝙥𝙖𝙘𝙞𝙚𝙣𝙩𝙚{Cor.RESET}")
    labels = [
        "CPF",
        "Nome do paciente",
        "Data de nascimento",
        "Idade do paciente",
        "Cep",
        "Telefone(cel)",
        "Sexo",
        "Tipo sanguíneo",
        "Alergia",
        "Problema de saúde crônico",
        "Atendimento prioritário",
        "Tipo de exame",
        "Data de exame"
    ]

    for label, valor in zip(labels, ficha_paciente.values()):
        print(f"{Cor.CINZA}{label}:{Cor.RESET} {valor}")

