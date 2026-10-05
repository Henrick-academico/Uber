from dataclasses import *

@dataclass
class item:
    valor:int | None 

class no:
    def __init__(self,x: item):
        self.dado: item = x
        self.prox: no | None = None
class lista:
    def __init__(self):
        self.primeiro = no(item(None))
        self.primeiro.prox = None

    def vazia(self) -> bool:
        return self.primeiro.prox == None

    def insere_final(self,x:item):
        aux = self.primeiro
        while aux.prox != self.primeiro and self.primeiro != None:
            aux = aux.prox
        novo = no(x)
        aux.prox = novo
        novo.prox = self.primeiro
    def imprime(self):
            aux = self.primeiro.prox
    
            print("[", end=" ")
    
            while aux != None:
                print(aux.dado.valor, end=" ")
                aux = aux.prox
    
            print("]")

        


 
   



