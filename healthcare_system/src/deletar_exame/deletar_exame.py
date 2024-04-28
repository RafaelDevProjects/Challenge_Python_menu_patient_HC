from healthcare_system.src.database import deletar_exames_por_cpf, verificar_cpf_existente
from healthcare_system.src.utils import escolher_opcao, imprimir_linha, Cor
def deletar_exame():
    print("""
█▀▀▄ █▀▀ █░░ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ 　 █▀▀ █░█ █▀▀█ █▀▄▀█ █▀▀ 
█░░█ █▀▀ █░░ █▀▀ ░░█░░ █▄▄█ █▄▄▀ 　 █▀▀ ▄▀▄ █▄▄█ █░▀░█ █▀▀ 
▀▀▀░ ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀ ▀░▀▀ 　 ▀▀▀ ▀░▀ ▀░░▀ ▀░░░▀ ▀▀▀""")
    imprimir_linha(60)
    while True:
        cpf = input("Digite o CPF do paciente para deletar os exames: ")
        if verificar_cpf_existente(cpf):
            opcao_confirmacao = input(f"{Cor.VERMELHO}Tem certeza de que deseja excluir os exames do paciente com CPF {cpf}? (s/n): {Cor.RESET}").strip().lower()
            confirmacao = escolher_opcao(opcao_confirmacao[0],["s","n"],f"{Cor.VERMELHO}Tem certeza de que deseja excluir os exames do paciente com CPF {cpf}? (s/n): {Cor.RESET}",f"{Cor.CINZA_CLARO}Escolha uma resposta valida{Cor.RESET}")
            if confirmacao == "s":
                deletar_exames_por_cpf(cpf)
            else:
                pass
        else:
            print(f"{Cor.CINZA}O CPF {cpf} não existe nos registros{Cor.RESET}")

        opcao_continuar = input("Deseja deletar mais exames? (s/n): ").strip().lower()
        continuar = escolher_opcao(opcao_continuar[0],["s","n"], "Deseja deletar mais exames? (s/n): ", f"{Cor.CINZA_CLARO}Escolha uma resposta valida{Cor.RESET}")
        if continuar != "s":
            print(f"{Cor.CINZA_CLARO}Saindo da área de exclusão de exames...{Cor.RESET}{'\n' * 5}")
            break