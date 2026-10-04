from dataclasses import *

@dataclass
class item:
    valor:int

class no:
    def __init__(self, x: item):
        self.dado: item=x
        self.prox: no | None = None
class fila:
    def __init__(self):
        self.inicio: no | None = None
        self.fim: no | None = None

    def vazia(self)->bool:
        return self.inicio == None

    def enfileira(self, x:item):
        novo = no(x)
        if not(self.vazia()):
            self.fim.prox = novo
        else:
            self.inicio = novo
        self.fim = novo

    def desinfileira(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            rem = self.inicio
            self.inicio=rem.prox
            if self.vazia():
                self.fim = self.inicio
            rem.prox = None
