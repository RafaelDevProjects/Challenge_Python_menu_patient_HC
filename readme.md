# Sistema de Agendamento e Cadastro de Pacientes

## Descrição
Este projeto consiste em um sistema simples para agendamento de exames e cadastro de pacientes. O sistema utiliza um banco de dados SQLite para armazenar as informações dos pacientes.

## Requisitos
- Python 3.x
- SQLite3 (incluso na maioria das instalações padrão do Python)

## Dependências
Não há dependências externas além das bibliotecas padrão do Python.

## Instruções de Uso

1. **Clonar o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. **Instalar Dependências (não há neste caso):**
    ```bash
    # Se necessário
    pip install -r requirements.txt
    ```

3. **Executar o Programa:**
    ```bash
    python nome_do_arquivo.py
    ```

4. **Funcionalidades do Sistema:**
    - **Cadastro de Pacientes:**
        - O sistema permite o cadastro de pacientes com informações como nome, CPF, idade, data de nascimento, endereço, telefone, sexo, tipo sanguíneo, alergias, problemas de saúde crônicos, se é prioritário e informações sobre o exame a ser realizado.

    - **Validação de CPF:**
        - Antes de inserir no banco de dados, o sistema valida se o CPF informado é válido.

    - **Prevenção de CPFs Duplicados:**
        - O sistema verifica se já existe um paciente com o mesmo CPF no banco de dados antes de inserir os dados. Se o CPF já estiver cadastrado, o sistema informa ao usuário e oferece a opção de atualizar as informações existentes.

    - **Banco de Dados SQLite:**
        - Os dados dos pacientes são armazenados em um banco de dados SQLite chamado `ficha_paciente.db`.

    - **Iteração com o Usuário:**
        - O sistema guia o usuário por meio de perguntas interativas para coletar as informações do paciente.

    - **Encerramento do Programa:**
        - Ao não querer cadastrar mais pacientes, o programa encerra, e você verá a mensagem "Programa encerrado."


## Autores
| Nome do Autor | RM |
|---------------|--------|
| Rafael de Almeida    | 554019 |
| Lucca    | 553678 |

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests.

