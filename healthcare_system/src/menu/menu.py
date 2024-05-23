from healthcare_system.src.database import exportar_exames_para_json
from healthcare_system.src.menu.utils_menu import *
from healthcare_system.src.agendar_exames.agendar_exames import *
from healthcare_system.src.agendar_exames.agendar_exames import agendar_exame
from healthcare_system.src.deletar_exame.deletar_exame import deletar_exame
from time import sleep


def menu():

    lista_opcoes = ['1','2','3',"4"]

    while True:
        print("""
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ██╗░█████╗░██████╗░
████╗░████║██╔════╝████╗░██║██║░░░██║  ██║██╔══██╗██╔══██╗
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ██║██║░░╚═╝██████╔╝
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██║██║░░██╗██╔══██╗
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ██║╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░╚════╝░╚═╝░░╚═╝""")
        imprimir_linha(60)
        mostrar_opcoes()
        escolha = escolher_opcao_lista(input("->"),lista_opcoes,"->",f"{Cor.CINZA_CLARO}Deve ser uma opção existente ex: {', '.join(lista_opcoes)}{Cor.RESET}")
        if escolha == "1":
            agendar_exame()
            sleep(2)
            limpar_console()
        elif escolha == "2":
            deletar_exame()
            sleep(2)
            limpar_console()
        elif escolha == "3":
            exportar_exames_para_json()
            sleep(2)
            limpar_console()
        elif escolha == "4":
            print(f"{Cor.ROSA}Obrigado por fazer parte do ICR{Cor.RESET} {Cor.CINZA_CLARO} \nEncerrando o programa...{Cor.RESET}")
            sleep(2)
            break