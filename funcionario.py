class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def decimo_terceiro(self, meses_trabalhados):
        return (self.salario / 12) * meses_trabalhados


f = Funcionario("Thiago", 3600)
print("13º salário:", f.decimo_terceiro(8))