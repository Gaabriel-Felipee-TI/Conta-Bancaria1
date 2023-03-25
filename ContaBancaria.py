class ContaCorrente:

  def __init__(self, nome, numero, cpf, saldo, limite):
    self.nome = nome
    self.numero = numero
    self.cpf = cpf
    self.saldo = saldo
    self.limite = limite

  @property
  def nome(self):
      return self.__nome

  @nome.setter
  def nome(self, novo_nome):
      self.__nome = novo_nome

  def extrato(self):
    return (f'Seu saldo disponivel é: R${self.saldo}')

  def deposito(self, valorx):
    self.saldo += valorx

  def pode_sacar(self, valor_saque):
    disponivel = self.saldo + self.limite
    return valor_saque <= disponivel

  def saque(self, valorx):
    if self.pode_sacar(valorx):
      self.saldo -= valorx
      return (f'você sacou R${valorx}')
    else:
      return ('valor indisponivel')

  def transferencia_pix(self, valorx, destino):
    if self.pode_sacar(valorx):
      self.saque(valorx)
      destino.deposito(valorx)
    else:
      return 'Seu saldo e insuficiente'
    return f' você fez uma trasferencia pix  '

  def saldo(self):
    return self.__saldo

from main import ContaCorrente

DiegoCorredeira = ContaCorrente('Diego', 12345, 1111111111, 5000, 3000)
GabrielFelipe = ContaCorrente('Gabriel', 13456, 111111122, 3000, 5000)
print(DiegoCorredeira.saque(7000))
print(DiegoCorredeira .transferencia_pix(1000, GabrielFelipe))
print(GabrielFelipe.extrato())
print(GabrielFelipe.extrato())
