import re
import sqlite3
from datetime import datetime

ficha_paciente = {}


class Cor:
    RESET = '\033[0m'
    CINZA = '\033[37m'
    VERDE = '\033[36m'
    ROSA = '\033[95m'
    AZUL = '\033[94m'
    CINZA_CLARO = '\033[90m'


def limpar_cores(texto_formatado):
    # Remove códigos de cor ANSI
    return re.sub(r'\033\[\d+m', '', texto_formatado)


def imprimir_linha(qnt):
    print(f'{Cor.ROSA}{"=" * qnt}{Cor.RESET}')


def imprimir_e_text_linha_bonita(msg):
    print(f"{Cor.ROSA}{'*' * (len(msg) + 4)}{Cor.RESET}")
    print(f"{Cor.ROSA}* {msg} *{Cor.RESET}")
    print(f"{Cor.ROSA}{'*' * (len(msg) + 4)}{Cor.RESET}")


def imprimir_tabela_tipos_sanguineos():
    print(f"{Cor.AZUL}Tipos Sanguíneos{Cor.RESET}")
    print(f"{Cor.AZUL}--------------------------{Cor.RESET}")
    print(f"{Cor.AZUL}A- | A+ | B+ | B- | AB+ | AB- | O+ | O-{Cor.RESET}")


def validar_cpf(cpf):
    # Função para validar um CPF
    cpf = list(map(int, cpf))

    if len(cpf) != 11 or len(set(cpf)) == 1:
        return False

    # Calcula o primeiro dígito verificador
    total = 0
    for i in range(9):
        total += cpf[i] * (10 - i)
    resto = total % 11
    digito_verificador1 = 0 if resto < 2 else 11 - resto

    # Verifica o primeiro dígito verificador
    if digito_verificador1 != cpf[9]:
        return False

    # Calcula o segundo dígito verificador
    total = 0
    for i in range(10):
        total += cpf[i] * (11 - i)
    resto = total % 11
    digito_verificador2 = 0 if resto < 2 else 11 - resto

    # Verifica o segundo dígito verificador
    if digito_verificador2 != cpf[10]:
        return False

    return True


def formata_numero_celular(numero):
    # Remover caracteres não numéricos
    numero = re.sub(r'\D', '', numero)

    # Formatar para (dd) 92118-4570
    return f'({numero[:2]}) {numero[2:7]}-{numero[7:]}'


def verifica_telefone(numero):
    # Formatar o número de celular
    numero_formatado = formata_numero_celular(numero)

    # Verificar se o número formatado está no padrão desejado
    if re.match(r'^\(\d{2}\) \d{5}-\d{4}$', numero_formatado):
        return numero_formatado
    else:
        print(f"{Cor.CINZA_CLARO}Formato de número de celular inválido!{Cor.RESET}")
        return None


def verifica_data(data):  # verifica o formato de data
    try:
        datetime.strptime(data, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def verifica_data_futura(data):  # verifica se é em uma data futura
    try:
        # Converter a string para um objeto datetime
        data_formatada = datetime.strptime(data, '%d-%m-%Y')

        # Verificar se a data é no futuro em relação à data atual
        data_atual = datetime.now()
        if data_formatada > data_atual:
            return True
        else:
            print(f"{Cor.CINZA_CLARO}Deve ser uma data futura. Tente novamente!{Cor.RESET}")
            return False

    except ValueError:
        print(f"{Cor.CINZA}Formato de data inválido. Deve ser preenchido neste formato: DD-MM-YYYY{Cor.RESET}")
        return False


def verifica_num(var, msg, alerta):
    while not var.isnumeric():
        print(alerta)
        var = input(msg)
    return int(var)


def escolher_opcao(var, lista_opcoes, msg, alerta):  # função para escolher entre sim ou não
    while var.lower() not in lista_opcoes:
        print(alerta)
        erro = input(msg).strip().lower()
        var = erro[0]
    return var


def escolher_opcao_lista(var, lista_opcoes, msg, alerta):  # função para escolher entre items de lista
    while var.lower() not in lista_opcoes:
        print(alerta)
        var = input(msg)
    return var


def dict_append(chave, valor):
    ficha_paciente[chave] = f"{Cor.VERDE}{valor}{Cor.RESET}"


def imprimir_ficha_completa():
    print(f"{Cor.VERDE}𝙛𝙞𝙘𝙝𝙖 𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙖 𝙙𝙤 𝙥𝙖𝙘𝙞𝙚𝙣𝙩𝙚{Cor.RESET}")
    print()

    labels = [
        "CPF",
        "Nome do paciente",
        "Idade do paciente",
        "Data de nascimento",
        "Endereço",
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
