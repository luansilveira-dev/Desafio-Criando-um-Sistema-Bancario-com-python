import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
from pathlib import Path
import os

ROOT_PATH = Path(__file__).parent

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
            
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        #if len(conta.historico.transacoes_do_dia()) >= 2:
            #print('Você excedeu numero de transações permitido para hoje !!')
            #return
        
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}: ({self.nome} {self.cpf})>'


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False
    
    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}, '{self.cliente.nome}')>"

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
    
    def gerar_ralatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao == None or transacao['tipo'].lower() == tipo_transacao.lower():
                yield transacao
        '''data_atual = datetime.utcnow().date()
        transacoes = []

        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()

            if data_atual == data_transacao:
                transacoes.append(transacao)

        return transacoes'''
    
    #def transacoes_do_dia(self):
        #return self.gerar_ralatorio()

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)





