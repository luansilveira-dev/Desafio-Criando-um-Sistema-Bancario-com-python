import os

def depositar(saldo, valor, extrato):
  if valor > 0:
    saldo += valor
    extrato += f'\n|  Depósito: R$ {valor:.2f}'
    print("Seu depósito foi realizado com sucesso !!")
  else:
    print("Esse valor é invalido !!")

  print('\nAperte ENTER para continuar...')
  input()
  return saldo, extrato
  

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

  return saldo, extrato, limite, numero_saques     

def extratos(saldo, /, *, extrato):
    print('''
|--------------------------------------------|
|                 EXTRATOS                   |
|--------------------------------------------|
    ''')
    print("|  Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n\n|  Saldo: R$ {saldo:.2f}")
    print("|--------------------------------------------|")
    print('\nAperte ENTER para continuar...')
    input()
  
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
  | [3] - Extrato.         | saques: {LIMITE_DE_SAQUES}/{numero_de_saques}
  | [4] - Sair.            | limite: R$ {limite:.2f}
  |------------------------|---------------------
       
  \nPara esclher uma opção, digite o número correspondente: '''
  opcao = int(input(menu))

  if opcao == 1:  ### Operação de Depósito
    valor_de_deposito = float(input('Informe o valor do depósito: '))

    saldo, extrato = depositar(saldo, valor_de_deposito, extrato)

  elif opcao == 2:  ## opeção de Saque

    valor_de_saque = float(input('\nInforme o valor do saque: '))

    saldo, extrato, limite, numero_de_saques = sacar( saldo=saldo, valor=valor_de_saque, extrato=extrato, limite=limite, numero_saques=numero_de_saques, limite_saque=LIMITE_DE_SAQUES)
    

  elif opcao == 3:
    os.system('cls' if os.name == 'nt' else 'clear')
    extratos(saldo, extrato=extrato)
  elif opcao == 4:
    print('Saindo...')
    break
  else:
    print('Opção inválida')
    print('\nAperte ENTER para continuar...')
    input()
  
  os.system('cls' if os.name == 'nt' else 'clear')
  
  
