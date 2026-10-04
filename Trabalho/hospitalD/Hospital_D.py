from dataclasses import *


@dataclass
class item:
    valor:int

class no:
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None
class fila:
    def __init__(self):
        self.inicio_geral: no | None = None
        self.fim_geral: no | None = None
        self.inicio: no | None = None
        self.fim: no|None = None
        self.posicao:int = 1
        self.controle:int = 0


    def vazia(self)->bool:
        return self.inicio_geral == None and self.inicio == None

    def enfileira_geral(self):
        novo = no(self.posicao)
        if self.inicio_geral != None:
            self.fim_geral.prox = novo
        else:
            self.inicio_geral = novo
        self.fim_geral = novo
        self.posicao+=1

    def enfileira_prioritaria(self):
        novo = no(self.posicao)

        if self.inicio != None:
            self.fim.prox = novo
        else:
            self.inicio = novo
        self.fim = novo
        self.posicao+=1
        self.controle+=1
        if self.controle >= 2:
                self.fim.prox =self.inicio_geral
                self.fim = self.fim_geral
                self.fim_geral = None
                self.inicio_geral = None
                self.controle = 0

    def desenfileira(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            if self.inicio != None:
                rem = self.inicio
                self.inicio=rem.prox
                if self.inicio == None:
                    self.fim = self.inicio
                rem.prox = None
                return rem.dado
            else:
                rem = self.inicio_geral
                self.inicio_geral = rem.prox
                if self.inicio_geral == None:
                    self.fim_geral = self.inicio_geral
                rem.prox = None
                return rem.dado
 

            
