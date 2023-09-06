from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda):
        self._nome = nome
        self._telefone = telefone
        self._renda = renda
            
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
         if type(novo_nome)  != str:
             raise TypeError("Tipo da variável deve ser str")
         self._nome = novo_nome

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        if type(novo_telefone) != str:
            raise TypeError("Tipo da variável deve ser str")
        self._telefone = novo_telefone
    
    @property
    def renda(self):
        return self._renda
    
    @abstractmethod
    def tem_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda):
        super().__init__(nome, telefone, renda)

    def tem_cheque_especial(self):
            return True

class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda):
        super().__init__(nome, telefone, renda)

    def tem_cheque_especial(self):
            return False

class ContaCorrente:
    def __init__(self, titular):
        self._saldo = 0.0
        self._extrato = []
        self._titulares = []
        self.adicionar_titular(titular)
   
    def adicionar_titular(self, titular):
        self._titulares.append(titular)
    
    def depositar(self, valor: float):
        self._saldo += valor
        self._extrato.append(f"Depósito de R$ {valor:.2f}")

    def sacar(self, valor: float):
        titular = self._titulares[0]
        if titular.tem_cheque_especial() == False:
            if valor <= self._saldo:
                self._saldo -= valor
                self._extrato.append(f"Depósito de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo Insuficiente")
            
        else:
            if valor <= self._saldo or (self._saldo - valor) <= titular._renda():
                 self._saldo -= valor
                 self._extrato.append(f"Depósito de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo Insuficiente")
            
    @property
    def saldo(self):
        return self._saldo

cliente_mulher = ClienteMulher("Cíntia Silva", "893123456", "20000")
cliente_homem = ClienteHomem("José Benicio", "0988876767", "3000")


conta1 = ContaCorrente(cliente_mulher)
conta2 = ContaCorrente(cliente_homem)

print(conta1.saldo)
print(conta2.saldo)

conta1.depositar(5000.0)
conta2.depositar(100.0)

print(conta1.saldo)
print(conta2.saldo)

conta1.sacar(1000)
conta2.depositar(500)

print(conta1.saldo)
print(conta2.saldo)