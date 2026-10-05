from dataclasses import *

@dataclass
class item:
    valor:int | None 

class no:
    def __init__(self,x: item):
        self.dado: item = x
        self.prox: no | None = None
        self.ant: no | None = None
class lista:
    def __init__(self):
        self.primeiro = no(item(None))
        self.primeiro.prox = None
        self.primeiro.ant = None

    def vazia(self) -> bool:
        return self.primeiro.prox == None

    def insere_inicio(self,x:item):
        aux = self.primeiro
        novo = no(x)
        if not(self.vazia()):
            aux.prox.ant = novo
            novo.prox = aux.prox           
        else:  
            novo.prox = self.primeiro
        self.primeiro.prox = novo
        novo.ant = self.primeiro
            



        


 
   



