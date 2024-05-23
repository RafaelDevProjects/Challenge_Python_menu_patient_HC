

# Hospital das Clínicas - Sistema de Cadastro de Pacientes

Este é um projeto em Python desenvolvido para o Hospital das Clínicas, que visa facilitar o cadastro de pacientes de forma organizada e eficiente.

## Funcionalidades Detalhadas

1. **Cadastro de Pacientes:**
   - O sistema permite o registro completo das informações dos pacientes, incluindo dados como CPF, idade, data de nascimento, telefone, sexo, tipo sanguíneo, alergias, doenças crônicas e prioridade.
   - Esses dados são essenciais para garantir um acompanhamento adequado do paciente e para que a equipe médica tenha acesso rápido a informações relevantes durante o atendimento.

2. **Validação de Dados:**
   - Antes de aceitar as informações inseridas pelo usuário, o sistema realiza validações para garantir que os dados estejam corretos e consistentes.
   - Por exemplo, verifica-se se o CPF possui o formato correto e se é um número válido, se a data de nascimento está no formato esperado e se é uma data válida, se o número de telefone possui a formatação adequada, entre outras validações.
   
3. **Validação de CEP com API:**
   - O sistema utiliza uma API de consulta de CEP para validar e obter o endereço a partir do CEP fornecido pelo usuário.
   - Essa funcionalidade garante que o endereço seja preenchido corretamente, economizando tempo e evitando erros de digitação.

4. **Agendamento de Exames:**
   - Além do cadastro básico do paciente, o sistema também permite o agendamento de exames.
   - O usuário pode escolher o tipo de exame que deseja realizar a partir de uma lista pré-definida, como raio-x, ultrassom, tomografia, entre outros.
   - O sistema também solicita a data desejada para realização do exame, garantindo uma melhor organização e planejamento das atividades do hospital.

5. **Priorização de Atendimento:**
   - Uma funcionalidade importante é a capacidade de identificar pacientes prioritários, como pessoas com deficiência (PCD), idosos ou gestantes.
   - Isso permite que a equipe médica priorize o atendimento desses pacientes, garantindo que recebam a assistência necessária de forma mais rápida e eficiente.

## Integração com o Banco de Dados

Este projeto utiliza um banco de dados SQLite para armazenar as informações dos pacientes e facilitar o gerenciamento das fichas médicas. A integração com o banco de dados permite que as informações sejam armazenadas de forma persistente, permitindo recuperação e atualização posterior.

### Estrutura do Banco de Dados
O banco de dados possui uma tabela chamada ficha_paciente, que contém os seguintes campos:

- cpf: CPF do paciente (chave primária)
- nome: Nome do paciente
- idade: Idade do paciente
- data_nascimento: Data de nascimento do paciente 
- endereco: Endereço do paciente
- telefone: Número de telefone do paciente
- sexo: Sexo do paciente
- tipo_sanguineo: Tipo sanguíneo do paciente
- alergia: Alergias do paciente
- saude_cronico: Problemas de saúde crônicos do paciente
- prioritario: Indicação de atendimento prioritário do paciente
- exame: Tipo de exame agendado para o paciente
- data_exame: Data do exame agendado para o paciente

### Operações no Banco de Dados
As principais operações realizadas no banco de dados são:

- Cadastro de Paciente: Ao cadastrar um novo paciente, suas informações são inseridas na tabela ficha_paciente.
- Atualização de Dados: Caso um paciente já exista no banco de dados, é possível atualizar suas informações, como endereço, telefone, etc.
- Consulta de Pacientes: É possível consultar as informações de todos os pacientes cadastrados no banco de dados.
- Agendamento de Exames: O sistema permite agendar exames para os pacientes, armazenando os detalhes do exame na tabela ficha_paciente.

### Conexão com o Banco de Dados
A conexão com o banco de dados é feita utilizando a biblioteca SQLite3 do Python. Os arquivos de banco de dados são criados na pasta data do projeto e são manipulados por meio de funções definidas no arquivo database.py.

Para mais detalhes sobre a estrutura do banco de dados e as operações disponíveis, consulte o código-fonte do projeto e a documentação das funções relacionadas ao banco de dados.

## Requisitos

- Python 3.x
- Biblioteca SQLite3 (já integrada no Python 3.x)

## Como Usar

1. **Clone este repositório em seu ambiente local:**
    ```bash
    git clone https://github.com/RafaelDevProjects/Challenge_Python_menu_patient_HC.git
    ```

2. **Execute o arquivo `main.py` para iniciar o programa:**
    ```bash
    python main.py
    ```

3. Siga as instruções fornecidas pelo programa para realizar o cadastro de pacientes.

## Nome e RM dos desenvolvedores do projeto

Nome: Rafael de Almeida Sigoli RM: 554019 

Nome: João Victor Seixos Flaitt RM: 553888 

Nome: Lucca Enrico Zanelato Calsolari RM: 553678 

Nome: Lucas Bertolassi Iori  RM: 553183

Nome: Miguel RM: 553009

