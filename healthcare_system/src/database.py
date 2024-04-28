# database.py
from utils import *
import sqlite3
from utils import escolher_opcao, Cor
import re

def criar_tabela():
    # Função para criar a tabela no banco de dados
    conn = sqlite3.connect('../data/ficha_paciente.db')
    cursor = conn.cursor()

    # SQL para criar a tabela se ela não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ficha_paciente (
            cpf TEXT PRIMARY KEY,
            nome TEXT,
            idade INTEGER,
            data_nascimento TEXT,
            endereco TEXT,
            telefone TEXT,
            sexo TEXT,
            tipo_sanguineo TEXT,
            alergia TEXT,
            saude_cronico TEXT,
            prioritario TEXT,
            exame TEXT,
            data_exame TEXT
        )
    ''')

    conn.commit()
    conn.close()

def inserir_ficha_no_banco(ficha_paciente):
    # Função para inserir a ficha do paciente no banco de dados
    conn = sqlite3.connect('../data/ficha_paciente.db')
    cursor = conn.cursor()

    # Verificar se já existe um registro com o mesmo CPF
    cursor.execute('SELECT * FROM ficha_paciente WHERE cpf = ?', (ficha_paciente['cpf'],))
    registro_existente = cursor.fetchone()

    if registro_existente:
        print(f"Já existe um paciente cadastrado com o CPF {ficha_paciente['cpf']}.")

        # Perguntar se deseja atualizar os dados
        while True:
            try:
                opcao_atualizar = input("Deseja atualizar os dados? (s/n): ").strip().lower()
                if not opcao_atualizar:
                    print(f"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")
                    continue
                opcao_atualizar = escolher_opcao(opcao_atualizar[0], ['s', 'n'], "Deseja atualizar os dados? (s/n): ",
                                                 f'{Cor.CINZA}Digite uma resposta válida!{Cor.RESET}')

                if opcao_atualizar == 's':
                    # Atualizar os dados para o mesmo CPF
                    cursor.execute('''
                           UPDATE ficha_paciente
                           SET nome=?, idade=?, data_nascimento=?, endereco=?, telefone=?, sexo=?, tipo_sanguineo=?,
                               alergia=?, saude_cronico=?, prioritario=?, exame=?, data_exame=?
                           WHERE cpf=?
                       ''', (
                        ficha_paciente['nome'], ficha_paciente['idade'], ficha_paciente['data_nascimento'],
                        ficha_paciente['endereco'], ficha_paciente['telefone'], ficha_paciente['sexo'],
                        ficha_paciente['tipo_sanguineo'], ficha_paciente['alergia'], ficha_paciente['saude_cronico'],
                        ficha_paciente['prioritario'], ficha_paciente['exame'], ficha_paciente['data_exame'],
                        ficha_paciente['cpf']
                    ))
                    print("Dados atualizados com sucesso! \n")
                else:
                    print("Cadastro não foi atualizado. \n")
                break
            except IndexError:
                print(f"{Cor.CINZA_CLARO}Por favor, digite uma opção válida.{Cor.RESET}")
    else:
        # Inserir os dados da ficha do paciente
        cursor.execute('''
            INSERT INTO ficha_paciente
            (cpf, nome, idade, data_nascimento, endereco, telefone, sexo, tipo_sanguineo, alergia,
             saude_cronico, prioritario, exame, data_exame)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            ficha_paciente['cpf'], ficha_paciente['nome'], ficha_paciente['idade'],
            ficha_paciente['data_nascimento'], ficha_paciente['endereco'], ficha_paciente['telefone'],
            ficha_paciente['sexo'], ficha_paciente['tipo_sanguineo'], ficha_paciente['alergia'],
            ficha_paciente['saude_cronico'], ficha_paciente['prioritario'], ficha_paciente['exame'],
            ficha_paciente['data_exame']
        ))

        print("Cadastro realizado com sucesso! \n")

    conn.commit()
    conn.close()

def deletar_exames_por_cpf(cpf):
    conn = sqlite3.connect('../data/ficha_paciente.db')
    cursor = conn.cursor()

    # Verificar se existe algum registro com o CPF fornecido
    cursor.execute('SELECT * FROM ficha_paciente WHERE cpf = ?', (cpf,))
    registro = cursor.fetchone()

    if registro:
        # Se o registro existir, deletar os exames associados a esse CPF
        cursor.execute('DELETE FROM ficha_paciente WHERE cpf = ?', (cpf,))
        conn.commit()
        print(f"{Cor.VERDE}Exames do paciente com CPF {cpf} deletados com sucesso.{Cor.RESET}")
    else:
        print(f"{Cor.CINZA}Não foram encontrados registros para o CPF {cpf}.{Cor.RESET}")

    conn.close()

def verificar_cpf_existente(cpf):
    conn = sqlite3.connect('../data/ficha_paciente.db')
    cursor = conn.cursor()

    # Verificar se a tabela existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ficha_paciente'")
    table_exists = cursor.fetchone()
    if not table_exists:
        print(f"{Cor.CINZA}A tabela 'ficha_paciente' ainda não foi criada, ainda não há nenhum exame cadastrado.{Cor.RESET}")
        conn.close()
        return False

    cursor.execute('SELECT COUNT(*) FROM ficha_paciente WHERE cpf = ?', (cpf,))
    count = cursor.fetchone()[0]

    conn.close()

    return count > 0
