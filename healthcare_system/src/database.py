# database.py
from utils import *
import sqlite3



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


def inserir_ficha_no_banco():
    global ficha_paciente
    # Função para inserir a ficha do paciente no banco de dados
    conn = sqlite3.connect('../data/ficha_paciente.db')
    cursor = conn.cursor()

    # Limpa a formatação dos dados
    dados_limpos = {chave: re.sub(r'\033\[\d+m', '', valor) for chave, valor in ficha_paciente.items()}

    # Verificar se já existe um registro com o mesmo CPF
    cursor.execute('SELECT * FROM ficha_paciente WHERE cpf = ?', (dados_limpos['cpf'],))
    registro_existente = cursor.fetchone()

    if registro_existente:
        print(f"Já existe um paciente cadastrado com o CPF {dados_limpos['cpf']}.")

        # Perguntar se deseja atualizar os dados
        opcao_atualizar = input("Deseja atualizar os dados? (s/n): ").strip().lower()
        opcao_atualizar = escolher_opcao(opcao_atualizar[0],['s','n'],"Deseja atualizar os dados? (s/n): ",f'{Cor.CINZA}Digite uma resposta valida!{Cor.RESET}')

        if opcao_atualizar == 's':
            # Atualizar os dados para o mesmo CPF
            cursor.execute('''
                UPDATE ficha_paciente
                SET nome=?, idade=?, data_nascimento=?, endereco=?, telefone=?, sexo=?, tipo_sanguineo=?,
                    alergia=?, saude_cronico=?, prioritario=?, exame=?, data_exame=?
                WHERE cpf=?
            ''', (
                dados_limpos['nome'], dados_limpos['idade'], dados_limpos['data_nascimento'],
                dados_limpos['endereco'], dados_limpos['telefone'], dados_limpos['sexo'],
                dados_limpos['tipo_sanguineo'], dados_limpos['alergia'], dados_limpos['saude_cronico'],
                dados_limpos['prioritario'], dados_limpos['exame'], dados_limpos['data_exame'], dados_limpos['cpf']
            ))
            print("Dados atualizados com sucesso!")
        else:
            print("Cadastro não foi atualizado.")

    else:
        # Inserir os dados da ficha do paciente
        cursor.execute('''
            INSERT INTO ficha_paciente
            (cpf, nome, idade, data_nascimento, endereco, telefone, sexo, tipo_sanguineo, alergia,
             saude_cronico, prioritario, exame, data_exame)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            dados_limpos['cpf'], dados_limpos['nome'], dados_limpos['idade'],
            dados_limpos['data_nascimento'], dados_limpos['endereco'], dados_limpos['telefone'],
            dados_limpos['sexo'], dados_limpos['tipo_sanguineo'], dados_limpos['alergia'],
            dados_limpos['saude_cronico'], dados_limpos['prioritario'], dados_limpos['exame'],
            dados_limpos['data_exame']
        ))

        print("Cadastro realizado com sucesso!")

    conn.commit()
    conn.close()
