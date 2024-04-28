from healthcare_system.src.agendar_exames.func_agendar_exames import *
from healthcare_system.src.database import criar_tabela, inserir_ficha_no_banco


def agendar_exame():
    while True:
        limpar_console()
        print("""
█▀▀█ █▀▀▀ █▀▀ █▀▀▄ █▀▀▄ █▀▀█ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀ █▀▀█ 　 █▀▀▄ █▀▀█ 　 █▀▀ █░█ █▀▀█ █▀▄▀█ █▀▀ 
█▄▄█ █░▀█ █▀▀ █░░█ █░░█ █▄▄█ █░▀░█ █▀▀ █░░█ ░░█░░ █░░█ 　 █░░█ █░░█ 　 █▀▀ ▄▀▄ █▄▄█ █░▀░█ █▀▀ 
▀░░▀ ▀▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀░░▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀▀ 　 ▀▀▀░ ▀▀▀▀ 　 ▀▀▀ ▀░▀ ▀░░▀ ▀░░░▀ ▀▀▀""")

        imprimir_linha(93)

        # pega CPF do paciente
        cpf = pega_cpf()
        dict_append("cpf", cpf)

        # pega o nome do paciente
        nome = input("Nome do paciente:")
        dict_append("nome", nome)

        # pega a data de nascimento
        data_nascimento = pega_data_nascimento()
        dict_append("data_nascimento", data_nascimento)

        # pega idade do paciente
        hoje = datetime.now()
        ano_nascimento = int(data_nascimento[-4:])
        idade = hoje.year - ano_nascimento
        dict_append("idade", idade)

        # pega o endereço
        endereco = input("Endereço do paciente:")
        dict_append("endereco", endereco)

        # pega o telefone ja formatado
        telefone_formatado = pega_telefone()
        dict_append("telefone", telefone_formatado)

        # Sexo do Paciente
        sexo = pega_sexo()
        dict_append("sexo", sexo)

        # Informações medicas
        # pega o tipo sanguíneo
        tipo_sanguineo = pega_tipo_sanguineo()
        dict_append("tipo_sanguineo", tipo_sanguineo)

        # pergunta se o paciente tem alergia
        alergia = pega_alergia()
        dict_append("alergia", alergia)

        # pergunta se tem problema crônico
        saude_cronico = pega_doenca_cronica()
        dict_append("saude_cronico", saude_cronico)

        # pergunta se é prioritário
        prioritario = pega_prioritario()
        dict_append("prioritario", prioritario)

        # Agendar o exame
        # pergunta o exame que ele irá fazer
        exame = pega_exame()
        dict_append("exame", exame)

        # pergunta a data do exame
        data_exame = pega_data_exame()
        dict_append("data_exame", data_exame)

        print()

        criar_tabela()  # Certifica-se de que a tabela existe no banco de dado
        inserir_ficha_no_banco(ficha_paciente)  # Insere a ficha do paciente no banco de dados

        limpar_console()
        imprimir_ficha_completa()
        print()

        # Pergunta ao usuário se ele quer cadastrar mais alguém.
        while True:
            try:
                opcao_cadastrar_mais = input("Deseja cadastrar mais uma pessoa? (s/n): ").strip().lower()
                if not opcao_cadastrar_mais:
                    print(f"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")
                    continue
                opcao_cadastrar_mais = escolher_opcao(opcao_cadastrar_mais[0], ["s", "n"],
                                                      "Deseja cadastrar mais uma pessoa? (s/n): ",
                                                      f"{Cor.CINZA_CLARO}Digite uma resposta válida!{Cor.RESET}")
                if opcao_cadastrar_mais == "n":
                    print(f"{Cor.CINZA_CLARO}Saindo da área de agendamento...{Cor.RESET}{'\n' * 5}")
                    break
                elif opcao_cadastrar_mais == "s":
                    break
            except IndexError:
                print(f"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")
        if opcao_cadastrar_mais == "n":
            break