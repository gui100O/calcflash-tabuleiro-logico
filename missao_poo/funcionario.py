from abc import ABC, abstractmethod

class Funcionario(ABC):
    def init(self, nome):
        self.nome = nome

@abstractmethod
def calcular_pagamento(self):
    pass
class FuncionarioCLT(Funcionario):
    def init(self, nome, salario):
        super().init(nome)
        self.salario = salario

def calcular_pagamento(self):
    return self.salario
class FuncionarioPJ(Funcionario):
    def init(self, nome, horas_trabalhadas, valor_hora):
        super().init(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

def calcular_pagamento(self):
    return self.horas_trabalhadas * self.valor_hora