# Desafio - Otimizando o Sistema Bancário com Python v2.0.0

## Objetivo do desafio
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para operações já existentes: sacar, depósito e visualizar extrato. Além disso, para a versão 2.0.0 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente e vincular com usuário.


## Funcionalidades do Sistema

### Menu do Sistema
O sistema apresenta um menu e status interativo com as seguintes opções:
```
  |------------------------|--------------------|
  |    MENU DO SISTEMA     |      Status        |
  |------------------------|--------------------
  | [1] - Depósito.        | Saldo: R$ 0.00
  | [2] - Saque.           |
  | [3] - Extrato.         | saques: 3/0
  | [4] - Sair.            | limite: R$ 500.00
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
A função deve receber argumentos apenas por nome(keyword only). Argumentos atilizados: saldo, valor, extrato, limite, numero_saques e limite_saque. Os retornos: saldo, extrato, limite, numero_saques  
```
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
  if valor > saldo:
    print('\nOperaçao falhou! Voce não tem saldo suficiente.')

  elif valor > limite:
    print('\nOperação falhou! O valor do saque excede o limite.')

  elif numero_saques >= limite_saque:
    print('\nOperação falhou! O número de saques diários excede o limite.')

  elif valor > 0:
    saldo -= valor
    numero_saques += 1
    limite -= valor
    extrato += f'\n|  Saque: R$ {valor:.2f}'
    print("Seu saque foi realizado com sucesso!!")

  else:
    print("Esse valor é invalido !!")
  
  print('\nAperte ENTER para continuar...')
  input()
```

## Operações do Extrato
A opção de extrato exibe um resumo das operações realizadas na conta, incluindo depósitos e saques. O extrato também mostra o saldo atual da conta.

## Sair do Sistema
Ao escolher a opção "Sair" no menu, o usuário encerra o sistema bancário.
