import textwrap
from classes import *
import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def pause():
  input('\nAperte ENTER para continuar...')

def menu():
    menu = """\n
    |------------------------|
    |    MENU DO SISTEMA     |
    |------------------------|
    | [1] - Depósito.        | 
    | [2] - Saque.           |
    | [3] - Extrato.         |
    | [4] - Nova Conta       |
    | [5] - Novo usuário.    |
    | [6] - Lista de contas. | 
    | [7] - Sair.            | 
    |------------------------|

    Para esclher uma opção, digite o número correspondente:"""
    return input(textwrap.dedent(menu))

def verificar_cliente(cpf, clientes):
    cliente_verificado = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente_verificado[0] if cliente_verificado else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas: 
        print('Cliente não possui conta !!')
        return
    
    cliente.contas[0]

def depositar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = verificar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado !!')
        return
    
    valor = float(input('Informe o valor do depósito'))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = verificar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado !!')
        return
    
    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = verificar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_clientes(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = verificar_cliente(cpf, clientes)

    if cliente:
        print('Cliente não encontrado !!')
        return
  
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

    print('Conta criada com sucesso!!')

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = verificar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\nConta criada com sucesso!")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []


    while True:
        opcao = menu()

        if opcao == '1':
            depositar(clientes)
            pause()
            clear()
        elif opcao == '2':
            sacar(clientes)
            pause()
            clear()
        elif opcao == '3':
            exibir_extrato(clientes)
            pause()
            clear()
        elif opcao == '4':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
            pause()
            clear()
        elif opcao == '5':
            criar_clientes(clientes)
            pause()
            clear()
        elif opcao == '6':
            listar_contas(contas)
            pause()
            clear()
        elif opcao == '7':
            break
        


main()