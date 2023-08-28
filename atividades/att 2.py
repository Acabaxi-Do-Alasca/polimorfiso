class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Produto(Item):
    def __init__(self, nome, preco, quantidade):
        super().__init__(nome, preco)
        self.quantidade = quantidade

    def calcular_valor(self):
        return self.preco * self.quantidade

class Servico(Item):
    def __init__(self, nome, preco, horas):
        super().__init__(nome, preco)
        self.horas = horas

    def calcular_valor(self):
        return self.preco * self.horas

# Exemplo de uso:
produto = Produto("Laptop", 1000, 2)
servico = Servico("Limpeza", 50, 3)

valor_produto = produto.calcular_valor()
valor_servico = servico.calcular_valor()

print(f"Produto: {produto.nome}, Preço Unitário: ${produto.preco}, Quantidade: {produto.quantidade}, Valor Total: ${valor_produto}")
print(f"Serviço: {servico.nome}, Preço por Hora: ${servico.preco}, Horas: {servico.horas}, Valor Total: ${valor_servico}")
