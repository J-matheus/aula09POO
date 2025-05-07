class Pessoa():
    def __init__(self,nome,peso,idade,comer,dormir,falar):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comer=comer
        self.falar=falar
        self.dormir=dormir

    def comendo(self):
        if self.falar == True:
                print(f"{self.nome} está falando portanto não pode comer e nem dormir.")
        elif self.dormir == True:
                 print(f"{self.nome} está dormindo portanto não pode comer e nem falar.")
    def falando(self):
        if self.comer == True:
            print(f"{self.nome} está comendo portanto não pode falar e nem dormindo.")
        elif self.dormir == True:
            print(f"{self.nome} está dormindo portanto não pode comer e nem falar.")
    def dormindo(self):
        if self.falar == True:
            print(f"{self.nome} está falando portanto não pode comer e nem dormindo.")
        elif self.comer == True:
            print(f"{self.nome} está comendo portanto não pode falar e nem dormir.")

# class Alimentos():
#     def __init__(self,pao,maca,batataDoce):
#         self.pao= pao
#         self.maca=maca
#         self.batataDoce=batataDoce
#     def pao(self):
#         paodeforma = True:
#         print("")