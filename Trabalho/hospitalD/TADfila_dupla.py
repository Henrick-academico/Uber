from dataclasses import *

@dataclass
class item:
    valor:int | None 

class no:
    def __init__(self,x: item):
        self.tipo: int = -1
        self.dado: item = x
        self.prox: no | None = None
        self.ant: no | None = None
class fila:
    def __init__(self):
        self.posicao: int = 0
        self.primeiro = no(item(None))
        self.ultimo = self.primeiro
        self.primeiro.prox = None
        self.primeiro.ant = None

    def vazia(self) -> bool:
        return self.primeiro.prox == None

    def enfileira_geral(self):
        self.posicao += 1
        novo = no(self.posicao)
        novo.tipo = 0
        self.ultimo.prox = novo
        novo.ant = self.ultimo
        self.ultimo = novo

    def enfileira_prioritaria(self):
        self.posicao += 1
        novo = no(self.posicao)
        aux: no = self.ultimo

        while aux != self.primeiro and aux.tipo>-1 and aux.tipo<2:
            if aux.tipo != -1:
                aux.tipo += 1
            aux = aux.ant
        novo.ant = aux
        
        if aux.prox != None:
            aux.prox.ant = novo
            novo.prox = aux.prox
        else:
            self.ultimo = novo
        aux.prox = novo
    
    def desenfileira(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            rem = self.primeiro.prox
            self.primeiro.prox = rem.prox
            if rem.prox != None:
                rem.prox.ant = self.primeiro
                rem.prox = None
            else:
                self.ultimo = self.primeiro
            rem.ant = None

            return rem.dado
            




        
       
        

    
    
