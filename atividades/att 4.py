class ContaBancaria():
    def calcular_juros(self):
        return 0

class ContaPoupanca(ContaBancaria):
    def calcular_juros(capital, juros, tempo):
        return capital + (capital * juros * tempo)

class ContaCorrente(ContaBancaria):
    def calcular_juros(capital, juros, tempo):
        return capital * ((1 + juros) ** tempo)

print(ContaPoupanca.calcular_juros(100, 0.10, 20))
print(ContaCorrente.calcular_juros(100, 0.10, 20))