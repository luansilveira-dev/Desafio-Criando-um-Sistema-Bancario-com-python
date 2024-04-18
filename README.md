# Desafio - Criando um Sistema Bancário com Python

## Objetivo do desafio
Fomos contratados por um grande banco para desenvolver o
seu novo sistema. Esse banco deseja modernizar suas
operações e para isso escolheu a linguagem Python. Para a
primeira versão do sistema devemos implementar apenas 3
operações: depósito, saque e extrato.


## Funcionalidades do Sistema

### Menu do Sistema
O sistema apresenta um menu e status interativo com as seguintes opções:
```
|------------------------|--------------------|
|    MENU DO SISTEMA     |      Status        |
|------------------------|--------------------
| [1] - Depósito.        | Saldo: R$ {saldo:.2f} 
| [2] - Saque.           |  
| [3] - Extrato.         | 
| [4] - Sair.            | limite: R$ {limite:.2f}
|------------------------|---------------------     
```

Para escolher uma opção, o usuário deve digitar o número correspondente à operação desejada.

### Variáveis do Sistema
Para armazenar e controlar os dados do usuário, o sistema utiliza as seguintes variáveis:

- `saldo = 0`: Saldo inicial da conta.
- `limite = 500`: Limite de saque diário.
- `extrato = ""`: String para armazenar o extrato das operações.
- `numero_de_saques = 0`: Número de saques realizados no dia.
- `LIMITE_DE_SAQUES = 3`: Limite máximo de saques diários.

## Operações do Depósito
Ao escolher a opção de depósito no menu, o usuário pode adicionar fundos à sua conta. O sistema valida o valor do depósito para garantir que seja um valor positivo e, em caso de sucesso, atualiza o saldo e registra a transação no extrato.

## Operações do Saque
A opção de saque permite que o usuário retire fundos de sua conta, respeitando o saldo disponível e o limite diário de saque. O sistema verifica as condições de saldo e limite antes de processar o saque e, em caso de sucesso, atualiza o saldo, o limite de saque e registra a transação no extrato.

## Operações do Extrato
A opção de extrato exibe um resumo das operações realizadas na conta, incluindo depósitos e saques. O extrato também mostra o saldo atual da conta.

## Sair do Sistema
Ao escolher a opção "Sair" no menu, o usuário encerra o sistema bancário.
