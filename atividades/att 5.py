class TransportePublico:
    def pegar_passageiro(self):
        return "Pegando"
    def largar_passageiro(self):
        return "Largando"

class Onibus(TransportePublico):
    def pegar_passageiro(self):
        print("Pegando passageiro11")
    def largar_passageiro(self):
        print("Largando passageiro12")

class Metro(TransportePublico):
    def pegar_passageiro(self):
        print(TransportePublico().pegar_passageiro(), "passageiro21")
    def largar_passageiro(self):
        print(TransportePublico().largar_passageiro(), "passageiro22")


onibus = Onibus()
metro = Metro()

onibus.pegar_passageiro()
onibus.largar_passageiro()

metro.pegar_passageiro()
metro.largar_passageiro()