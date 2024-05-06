import os
import textwrap
from datetime import datetime
from pathlib import Path

from classes import ContaCorrente, ContaIterador, Deposito, PessoaFisica, Saque

ROOT_PATH = Path(__file__).parent


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nAperte ENTER para continuar...")


def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.utcnow().strftime("%d/%m/%Y - %H:%M:%S")

        with open(ROOT_PATH / "data-log" / "log.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"[{data_hora} Função: '{func.__name__}' executadas com argumentos {args} e {kwargs}."
                f"Retornou {resultado}\n]"
            )
        print(f"{data_hora}: {func.__name__.upper()}")

        return resultado

    return envelope


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

    Para esclher uma opção, digite o número correspondente: """
    return input(textwrap.dedent(menu))


def verificar_cliente(cpf, clientes):
    cliente_verificado = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente_verificado[0] if cliente_verificado else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta !!")
        return

    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = verificar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado! ")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = verificar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado !!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return conta

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = verificar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado! ")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_ralatorio():
        tem_transacao = True
        extrato += f"\n\n{transacao['data']}\n\t{transacao['tipo']}: R$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações."

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_clientes(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = verificar_cliente(cpf, clientes)

    if cliente:
        print("Cliente não encontrado !!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print("\n Cliente criado com sucesso! ")


@log_transacao
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
    for conta in ContaIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():

    clientes = []
    contas = []

    while True:
        opcao = menu()
        match opcao:
            case "1":
                depositar(clientes)
                pause()
                clear()
            case "2":
                sacar(clientes)
                pause()
                clear()
            case "3":
                exibir_extrato(clientes)
                pause()
                clear()
            case "4":
                numero_conta = len(contas) + 1
                criar_conta(numero_conta, clientes, contas)
                pause()
                clear()
            case "5":
                criar_clientes(clientes)
                pause()
                clear()
            case "6":
                listar_contas(contas)
                pause()
                clear()
            case "7":
                break


main()
