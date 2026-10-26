from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class item:
    valor: float

class no:
    def __init__(self, dado: item):
        self.esq: no | None = None
        self.dir: no | None = None
        self.dado: item = dado

class arvore:
    def __init__(self):
        self.raiz: no | None = None

    def vazia(self):
        return self.raiz == None
    
    def PreOrdem(self, no):
        if no != None:
            print(no.dado)
            self.PreOrdem(no.esq)
            self.PreOrdem(no.dir)

    def InOrdem(self, no):
        if no != None:
            self.InOrdem(no.esq)
            print(no.dado)
            self.InOrdem(no.dir)            

    def PosOrdem(self, no):
        if no != None:
            self.PosOrdem(no.esq)
            self.PosOrdem(no.dir)      
            print(no.dado)                         
