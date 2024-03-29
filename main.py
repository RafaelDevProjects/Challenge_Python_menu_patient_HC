from datetime import datetime
import re
import sqlite3
from func.funcoes import *
from func.funcoes_main import *


def main():
    while True:
        limpar_console()
        print("""
█▀▀█ █▀▀▀ █▀▀ █▀▀▄ █▀▀▄ █▀▀█ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀█ 　 █▀▀▄ █▀▀█ 　 █▀▀ █░█ █▀▀█ █▀▄▀█ █▀▀ 
█▄▄█ █░▀█ █▀▀ █░░█ █░░█ █▄▄█ █░▀░█ █▀▀ █░░█ ░░█░░ █░░█ 　 █░░█ █░░█ 　 █▀▀ ▄▀▄ █▄▄█ █░▀░█ █▀▀ 
▀░░▀ ▀▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀░░▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ 　 ▀▀▀░ ▀▀▀▀ 　 ▀▀▀ ▀░▀ ▀░░▀ ▀░░░▀ ▀▀▀""")
        
        imprimir_linha(93)

        
        global ficha_paciente
        ficha_paciente = []


        #pega CPF do paciente
        cpf = pega_cpf()
        lista_append(cpf)

        # pega o nome do paciente
        nome = input("Nome do paciente:")
        lista_append(nome)

        # pega a idade do paciente
        idade = pega_idade()
        lista_append(idade)

        # pega a data de nascimento
        data_nascimento = pega_data_nascimento()
        lista_append(data_nascimento)

        # pega o endereço
        endereco = input("Endereço do paciente:")
        lista_append(endereco)

        # pega o telefone ja formatado
        telefone_formatado = pega_telefone()
        lista_append(telefone_formatado)

        # Sexo do Paciente
        sexo = pega_sexo()
        lista_append(sexo)

        #Informações medicas
        # pega o tipo sanguíneo
        tipo_sanguineo = pega_tipo_sanguineo()
        lista_append(tipo_sanguineo)

        # pergunta se o paciente tem alergia
        alergia = pega_alergia()
        lista_append(alergia)

        # pergunta se tem problema crônico
        saude_cronico = pega_doenca_cronica()
        lista_append(saude_cronico)

        # pergunta se é prioritário
        prioritario = pega_prioritario()
        lista_append(prioritario)

        #Agendar o exame
        # pergunta o exame que ele irá fazer
        exame = pega_exame()
        lista_append(exame)

        # pergunta a data do exame
        data_exame = pega_data_exame()
        lista_append(data_exame)


        criar_tabela()  # Certifica-se de que a tabela existe no banco de dado
        inserir_ficha_no_banco()  # Insere a ficha do paciente no banco de dados

        limpar_console()
    
        imprimir_ficha_completa()
        print(f"Muito Obrigado por utilizar os serviços do {Cor.AZUL}HC{Cor.RESET}")


        #Pergunta ao usuário se ele quer cadastrar mais alguém.
        opcao_cadastrar_mais = input('Deseja Cadastrar mais uma pessoa? ').strip().lower()
        opcao_cadastrar_mais = escolher_opcao(opcao_cadastrar_mais[0],["s", "n"], 'Deseja Cadastrar mais uma pessoa? ', f"{Cor.CINZA_CLARO}Digite uma resposta valida!!{Cor.RESET}" )
        if opcao_cadastrar_mais != "s":
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
