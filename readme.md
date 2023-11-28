# HealthConnect

## Descrição
O HealthConnect é um sistema simples para agendamento de exames e criação de ficha do paciente. Ele permite que os usuários forneçam informações detalhadas sobre o paciente, agendem exames e armazenem esses dados em um banco de dados SQLite.

## Requisitos
- Python 3.x
- Biblioteca SQLite3 (já incluída no Python)
- Terminal com suporte a cores ANSI (para melhor experiência de usuário)


## Dependências
Nenhuma

## Instruções de Uso
1. **Clone o repositório:** `git clone https://github.com/seu-usuario/HealthConnect.git`
2. **Navegue até o diretório do projeto:** `cd main.py`
3. **Execute o script principal:** `python main.py`
4. **Siga as instruções na linha de comando para:**
   - Preencher detalhes do paciente, incluindo nome, idade, data de nascimento, endereço, etc.
   - Agendar exames, escolhendo entre opções como raio-x, ultrassom, tomografia, ressonância, ecocardiograma.
   - Confirmar se o paciente possui alergias ou problemas de saúde crônicos.
   - Identificar se o paciente é prioritário e em qual categoria (pessoa com deficiência, idoso, gestante).
   - Definir a data para realização do exame.

## Funcionalidades
1. **Cadastro de Pacientes:**
   - Coleta informações detalhadas do paciente.
   - Formatação automática de números de telefone e validação de data de nascimento.

2. **Agendamento de Exames:**
   - Escolha entre uma variedade de exames disponíveis.
   - Defina a data para a realização do exame, garantindo que seja uma data futura.

3. **Armazenamento Seguro de Dados:**
   - Utiliza um banco de dados SQLite para armazenar as informações do paciente.
   - Garante persistência dos dados para consultas futuras.

4. **Interface de Linha de Comando Intuitiva:**
   - Mensagens claras e instruções para orientar o usuário durante o processo.
   - Tratamento de erros para garantir uma experiência de usuário suave.

## Autores
| Nome do Autor | RM |
|---------------|--------|
| Rafael de Almeida    | 554019 |
| Lucca    | 553678 |

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests.

