import os  


def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def pause():
  print('\nAperte ENTER para continuar...')
  input()
  
def menu(saldo, limite_saque, numero_saques, limite):
  menu = f'''
  |------------------------|--------------------|
  |    MENU DO SISTEMA     |      Status        |
  |------------------------|--------------------
  | [1] - Depósito.        | Saldo: R$ {saldo:.2f} 
  | [2] - Saque.           |  
  | [3] - Extrato.         | 
  | [4] - Nova Conta       | 
  | [5] - Novo usuário.    | 
  | [6] - Lista de contas. | saques: {limite_saque}/{numero_saques}
  | [7] - Sair.            | limite: R$ {limite:.2f}
  |------------------------|---------------------
       
  \nPara esclher uma opção, digite o número correspondente: '''
  
  return menu 

def depositar(saldo, valor, extrato):
  if valor > 0:
    saldo += valor
    extrato += f'\n|  Depósito: R$ {valor:.2f}'
    print("Seu depósito foi realizado com sucesso !!")
  else:
    print("Esse valor é invalido !!")

  pause()
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
    pause()

def novo_usuario(usuario):
  print('----------------------------------------------')
  print('|               Novo Usuario                 |')
  print('----------------------------------------------')
  cpf = input('| CPF: ')
  if verificar_usuario(cpf, usuario):
    print('---------------------------------------------')
    print('  Esse usuário já existe !')
    return

  nome = input('| Nome Completo: ')
  data_nascimento = input('| Data de Nascimento (dd-mm-aaaa): ')
  endereco = input('| Endereço (Logradouro, Nº - Bairro, Cidade/Sigla): ')

  usuario.append({'cpf':cpf, 'nome': nome, 'data_nascimento':data_nascimento, 'endereco': endereco})
  print('---------------------------------------------')
  print('   Usuário cadastrado com Sucesso !')

def verificar_usuario(cpf, usuarios):
  verificador_usuario = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
  return verificador_usuario[0] if verificador_usuario else None

def nova_conta(agencia, numero_conta, usuario):
  print('----------------------------------------------')
  print('|               Nova Conta                   |')
  print('----------------------------------------------')
  cpf = input('| CPF: ')

  if verificar_usuario(cpf, usuario):
    print('--------------------------------------------')
    print('  Conta criada com sucesso !')
    return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
  print('----------------------------------------------')
  print(' Usuario não encotrado !')

def lista_contas(contas):
  for conta in contas:
    linha = f'''
    Agência: {conta['agencia']}
    C/C: {conta['numero_conta']}
    Titular: {conta['usuario']['nome']}
    '''
    print('-' * 100)
    print((linha))

def main():
  saldo = 0
  limite = 500
  extrato = ""
  numero_de_saques = 0
  usuarios = []
  contas = []
  LIMITE_DE_SAQUES = 3
  AGENCIA = '0001'

  while True:

    opcao = input(menu(saldo, LIMITE_DE_SAQUES, numero_de_saques, limite))

    if opcao == '1':  ### Operação de Depósito
      valor_de_deposito = float(input('Informe o valor do depósito: '))

      saldo, extrato = depositar(saldo, valor_de_deposito, extrato)

    elif opcao == '2':  ## opeção de Saque

      valor_de_saque = float(input('\nInforme o valor do saque: '))

      saldo, extrato, limite, numero_de_saques = sacar( saldo=saldo, valor=valor_de_saque, extrato=extrato, limite=limite, numero_saques=numero_de_saques, limite_saque=LIMITE_DE_SAQUES)
      
    elif opcao == '3':
      clear()
      extratos(saldo, extrato=extrato)

    elif opcao == '4':
      clear()
      numero_conta = len(contas) + 1
      conta = nova_conta(AGENCIA, numero_conta, usuarios )
      if conta: 
        contas.append(conta)
      pause()

    elif opcao == '5':
      clear()
      novo_usuario(usuarios)
      pause()

    elif opcao == '6':
      clear()
      lista_contas(contas)
      pause()
    elif opcao == '7':
      print('Saindo ...')
      break

    else:
      print('Opção inválida')
      print('\nAperte ENTER para continuar...')
      input()
    
    clear()
  
if __name__ == '__main__':
  main()  
