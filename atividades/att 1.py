class AnimalAquatico:
    def nadando(self):
        print("O animal aquático está nadando.")

class Peixe(AnimalAquatico):
    def nadando(self):
        print("O peixe está nadando e movendo suas barbatanas.")

class Tartaruga(AnimalAquatico):
    def nadando(self):
        print("A tartaruga está nadando lentamente e escondendo-se dentro da concha.")

animais_aquaticos = [Peixe(), Tartaruga(), Peixe(), Tartaruga()]

for animal in animais_aquaticos:
    animal.nadando()
