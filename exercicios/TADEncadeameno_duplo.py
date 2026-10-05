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
        self.ultimo = self.primeiro
        self.primeiro.prox = None
        self.primeiro.ant = None

    def vazia(self) -> bool:
        return self.primeiro.prox == None

    def busca(self, x:int)->int|None:
        i = 0
        aux = self.primeiro
        retorno: int|None = None

        while aux != None and x != aux.dado.valor :
            i+=1
            aux = aux.prox
        if aux != None and x == aux.dado.valor:
            retorno = i 
        return retorno

    def insere_ini(self, x: item) -> bool:
        if self.busca(x.valor) == None:
            novo = no(x)
            novo.prox = self.primeiro.prox
            novo.ant = self.primeiro
            if self.primeiro.prox != None:
                self.primeiro.prox.ant = novo
            else:
                self.ultimo = novo
            self.primeiro.prox = novo
            return True
        else:
            return False
        

    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.primeiro.prox
            self.primeiro.prox = rem.prox
            if rem.prox != None:
                rem.prox.ant = self.primeiro
            else:
                self.ultimo = self.primeiro
            rem.prox = None
            rem.ant = None
            return True
        else:
            return False
    def remove_item(self,x:int):
        i = self.busca(x)
        if i != None:
            aux: no = self.primeiro
            for n in range(i):
                aux = aux.prox
            aux.ant.prox = aux.prox
            if aux.prox!=None:
                aux.prox.ant = aux.ant
                aux.prox = None
            else:
                self.ultimo = aux.ant
            aux.ant = None
        else:
            ValueError("Item não existe.")
    def imprime(self):
        aux = self.primeiro.prox

        print("[", end=" ")

        while aux != None:
            print(aux.dado.valor, end=" ")
            aux = aux.prox

        print("]")



