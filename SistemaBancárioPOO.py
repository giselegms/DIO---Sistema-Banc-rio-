from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
    def __init__(self, endereco):
        self.endereco= endereco
        self.contas= []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf= cpf
        self.nome= nome
        self.data_nascimento= data_nascimento


class Conta:
    def __init__(self, numero, cliente):
        self.saldo= 0
        self.numero= numero
        self.agencia= "0001"
        self.cliente= cliente
        self.historico= Historico()

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
        return self._histoico
    

    def sacar(self, valor):

        saldo= self.saldo
        excedeu_saldo= valor>saldo

        if excedeu_saldo:
            print ("Operação negada!")
        elif valor>0:
            self._saldo -= valor
            print ("Saque de R$ {:.2f} realizado com sucesso!".format(valor))
            return True
        
        else:
            print ("Operação inválida!")
        return False    

    def depositar(self, valor):
        if valor>0:
            self._saldo+=valor
            print ("Depósito realizado com sucesso!")
        else:
            print ("Operação negada!")
            return False
        return True
    


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite= limite
        self.limite_saques= limite_saques

    def sacar (self, valor):
        numero_saques= len([transacao for transacao in self.historico.transacoes
                            if transacao["tipo"]=="Saque"])
        excedeu_limite= valor > self.limite
        excedeu_saques= numero_saques >= self.limite_saques

        if excedeu_limite:
            print ("Operação negada!")
        elif excedeu_saques:
            print ("Operação negada!")
        else:
            return super().sacar(valor)
        return False
    

class Historico:
    def __init__(self):
        self._transacoes=[]

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append ({
            "tipo": transacao.__class.__.__name__,
            "valor": transacao.valor,

        })
        

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
        self._valor= valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso_transacao= conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor= valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao= conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)