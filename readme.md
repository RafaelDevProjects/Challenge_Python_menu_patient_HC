

# Hospital das Clínicas - Sistema de Cadastro de Pacientes

Este é um projeto em Python desenvolvido para o Hospital das Clínicas, que visa facilitar o cadastro de pacientes de forma organizada e eficiente.

## Funcionalidades

O projeto oferece as seguintes funcionalidades:

1. **Cadastro de Pacientes:** Permite o registro de informações dos pacientes, como CPF, idade, data de nascimento, telefone, sexo, tipo sanguíneo, alergias, doenças crônicas, prioridade e agendamento de exames.

2. **Validação de Dados:** Garante que as informações inseridas sejam válidas, como CPF, data de nascimento, telefone, entre outros.

3. **Limpeza de Console:** Função para limpar o console do usuário, proporcionando uma melhor experiência de uso.


## Funcionalidades Detalhadas

1. **Cadastro de Pacientes:**
   - O sistema permite o registro completo das informações dos pacientes, incluindo dados como CPF, idade, data de nascimento, telefone, sexo, tipo sanguíneo, alergias, doenças crônicas e prioridade.
   - Esses dados são essenciais para garantir um acompanhamento adequado do paciente e para que a equipe médica tenha acesso rápido a informações relevantes durante o atendimento.

2. **Validação de Dados:**
   - Antes de aceitar as informações inseridas pelo usuário, o sistema realiza validações para garantir que os dados estejam corretos e consistentes.
   - Por exemplo, verifica-se se o CPF possui o formato correto e se é um número válido, se a data de nascimento está no formato esperado e se é uma data válida, se o número de telefone possui a formatação adequada, entre outras validações.

3. **Agendamento de Exames:**
   - Além do cadastro básico do paciente, o sistema também permite o agendamento de exames.
   - O usuário pode escolher o tipo de exame que deseja realizar a partir de uma lista pré-definida, como raio-x, ultrassom, tomografia, entre outros.
   - O sistema também solicita a data desejada para realização do exame, garantindo uma melhor organização e planejamento das atividades do hospital.

4. **Priorização de Atendimento:**
   - Uma funcionalidade importante é a capacidade de identificar pacientes prioritários, como pessoas com deficiência (PCD), idosos ou gestantes.
   - Isso permite que a equipe médica priorize o atendimento desses pacientes, garantindo que recebam a assistência necessária de forma mais rápida e eficiente.

5. **Limpeza de Console:**
   - Uma pequena, mas útil funcionalidade, é a capacidade de limpar o console do usuário.
   - Isso proporciona uma interface mais limpa e organizada, melhorando a experiência do usuário durante a interação com o sistema.

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

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a Licença MIT.

