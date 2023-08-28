class Calculo:
    def calcular(self, *args):
        pass

class Soma(Calculo):
    def calcular(self, *args):
        resultado = sum(args)
        return resultado

class Multiplicacao(Calculo):
    def calcular(self, *args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado


calculadora = Calculo()
resultado_soma = calculadora.calcular(1, 2, 3, 4, 5)
print(f"Soma: {resultado_soma}")

calculadora = Calculo()
resultado_multiplicacao = calculadora.calcular(1, 2, 3, 4, 5)
print(f"Multiplicação: {resultado_multiplicacao}")
