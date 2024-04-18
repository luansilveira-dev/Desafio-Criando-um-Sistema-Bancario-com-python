import os

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3


while True:
  
  menu = f'''
  |------------------------|--------------------|
  |    MENU DO SISTEMA     |      Status        |
  |------------------------|--------------------
  | [1] - Depósito.        | Saldo: R$ {saldo:.2f} 
  | [2] - Saque.           |  
  | [3] - Extrato.         | 
  | [4] - Sair.            | limite: R$ {limite:.2f}
  |------------------------|---------------------       
  \nPara esclher uma opção, digite o número correspondente: '''
  opcao = int(input(menu))
  if opcao == 1:  ### Operação de Depósito
    valor_de_deposito = float(input('Informe o valor do depósito: '))
    if valor_de_deposito > 0:
      saldo += valor_de_deposito
      extrato += f' \n|  Depósito: R$ {valor_de_deposito:.2f}'

  elif opcao == 2:  ## opeção de Saque

    valor_de_saque = float(input('\nInforme o valor do saque: '))
    ## Variáveis de comparação
    excedeu_valor = valor_de_saque > saldo
    excedeu_limite = valor_de_saque > limite
    excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES
    
    if excedeu_valor:
      print('\nOperaçao falhou! Voce não tem saldo suficiente.')
    elif excedeu_limite:
      print('\nOperação falhou! O valor do saque excede o limite.')
    elif excedeu_saque:
      print('\nOperação falhou! O número de saques diários excede o limite.')
    elif valor_de_saque > 0:
      saldo -= valor_de_saque
      numero_de_saques += 1
      extrato += f' \n|  Saque: R$ {valor_de_saque:.2f}'
      limite -= valor_de_saque
    print('\nAperte ENTER para continuar...')
    input()

  elif opcao == 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
|--------------------------------------------|
|                 EXTRATOS                   |
|--------------------------------------------|
    ''')
    print("|  Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n|  Saldo: R$ {saldo:.2f}")
    print("|--------------------------------------------|")
    print('\nAperte ENTER para continuar...')
    input()
  elif opcao == 4:
    print('Saindo...')
    break
  else:
    print('Opção inválida')
  
  os.system('cls' if os.name == 'nt' else 'clear')
  
  
