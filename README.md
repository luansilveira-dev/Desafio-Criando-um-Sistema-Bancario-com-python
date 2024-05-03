# Desafio - Modelando o Sistema Bancário em POO com Python v3.1.0

## Objetivo do desafio
Com os novos conhecimentos adquiridos sobre decoradores, geradores e integradores você foi encarregado de implementar as seguintes funcionalidades no sistema.
-	Decorador de log
-	Gerador de relatórios
-	Iterado personalizado 

## Funcionalidades do Sistema

### Menu do Sistema
O sistema apresenta um menu e status interativo com as seguintes opções:
```
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

Para esclher uma opção, digite o número correspondente:
```

Para escolher uma opção, o usuário deve digitar o número correspondente à operação desejada.

## Decorador de log 
Implementar um decorador que seja aplicado a todas as funções de transações (depósito, criação de conta, etc..). Esse decorador deve registrar (printar) a data e hora de cada transação. 

```
def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f'{datetime.now()}: {func.__name__.upper()}')

        return resultado

    return envelope
```

```
@log_transacao
def depositar(clientes):
    pass

@log_transacao
def sacar(clientes):
    pass

@log_transacao
def exibir_extrato(clientes):
    pass

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    pass
```

## Gerador de relatórios 
Crie um gerador que permita iterar sobre a transação de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve ter uma forma de filtrar as transações baseado no seu tipo (exemplo, apenas saques e apenas depósitos).
```
def gerar_ralatorio(self, tipo_transacao=None):
    for transacao in self._transacoes:
        if tipo_transacao == None or transacao['tipo'].lower() == tipo_transacao.lower():
            yield transacao
```
```
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
```
## Iterado personalizado 
Implementar um iterado personalizado ContaIterador que permite iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual).
```
class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0 

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f'''
                    Agência:\t{conta.agencia}
                    Número:\t\t{conta.numero}
                    Titular:\t{conta.cliente.nome}
                    Saldo:\t\tR$ {conta.saldo:.2f}
            '''
        except IndexError:
            raise StopIteration
        
        finally:
            self._index += 1
```

```
def listar_contas(contas):
    for conta in ContaIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))
```
