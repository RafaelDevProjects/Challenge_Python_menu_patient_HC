from healthcare_system.src.utils import Cor

def mostrar_opcoes():
    print(f"{Cor.AZUL}Selecione uma opção:{Cor.RESET}")
    print(f"{Cor.VERDE}1. Cadastrar Exame{Cor.RESET}")
    print(f"{Cor.VERDE}2. Deletar Exame{Cor.RESET}")
    print(f"{Cor.VERDE}3. Exportar Exames para JSON{Cor.RESET}")
    print(f"{Cor.VERDE}4. Sair do Programa{Cor.RESET}")