from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class item:
    chave: int
    valor: float

class no:
    def __init__(self, dado: item):
        self.esq: no | None = None
        self.dir: no | None = None
        self.altura: int = 1
        self.dado: item = dado

class arvore_avl:
    def __init__(self):
        self.raiz: no | None = None

    def vazia(self):
        return self.raiz == None

    def insere(self, x: item):
        self.raiz = self.insere_no(self.raiz, x)
    
    def busca(self, ch: int) -> item | None:
        no_encontrado = self.busca_no(self.raiz, ch)
        if no_encontrado != None:
            return no_encontrado.dado
        else:
            return None
    
    def remove(self, chave: int):
        self.raiz = self.remove_no(self.raiz, chave)

    def busca_no(self, n: no | None, chave: int) -> no | None:
        if n == None:
            return None
        elif chave > n.dado.chave:
            return self.busca_no(n.dir, chave)
        elif chave < n.dado.chave:
            return self.busca_no(n.esq, chave)
        else:
            return n
        
    def insere_no(self, n: no | None, x: item) -> no:
        if n == None:
            return no(deepcopy(x))
        elif x.chave > n.dado.chave:
            n.dir = self.insere_no(n.dir, x)
        elif x.chave < n.dado.chave:
            n.esq = self.insere_no(n.esq, x)
        return self.balanceia(n)

    def maior(self, n: no) -> no:
        if n.dir == None:
            return n
        else:
            return self.maior(n.dir)
    
    def remove_no(self, n: no | None, chave: int) -> no | None:
        if n != None:
            if n.dado.chave < chave:
                n.dir = self.remove_no(n.dir, chave)
            elif n.dado.chave > chave:
                n.esq = self.remove_no(n.esq, chave)
            else:
                if n.esq != None and n.dir != None:
                    antecessor = self.maior(n.esq)
                    n.dado = antecessor.dado
                    n.esq = self.remove_no(n.esq, antecessor.dado.chave)
                elif n.esq == None:
                    n = n.dir
                else:
                    n = n.esq 
        if n != None:
            n = self.balanceia(n)
        return n
    
    def altura_no(self, n: no | None) -> int:
        if n == None:
            return 0
        altura_sad = n.dir.altura if n.dir != None else 0
        altura_sae = n.esq.altura if n.esq != None else 0
        return max(altura_sae, altura_sad) + 1
    
    
    def rotacao_esq(self, p: no) -> no:
        q = p.dir
        p.dir = q.esq
        q.esq = p
        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        return q
    
 
    def rotacao_dupla_esq(self, p: no) -> no:
        q = p.dir
        w = q.esq
        q.esq = w.dir
        p.dir = w.esq
        w.dir = q
        w.esq = p

        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        w.altura = self.altura_no(w)
        return w
    
    def rotacao_dir(self, p:no) -> no:
        q = p.esq
        p.esq = q.dir
        q.dir = p
        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        return q   
         
    def rotacao_dupla_dir(self, p: no) -> no:
        q = p.esq
        w = q.dir
        q.dir = w.esq
        p.esq = w.dir
        w.esq = q
        w.dir = p

        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        w.altura = self.altura_no(w)

        return w
     
    def balanceia(self, n: no | None) -> no | None:
        if n != None:
            asd = self.altura_no(n.dir)
            ase = self.altura_no(n.esq)
            if asd > ase + 1:
                if self.altura_no(n.dir.esq) > self.altura_no(n.dir.dir):
                    return self.rotacao_dupla_esq(n)
                else:
                    return self.rotacao_esq(n)
            elif ase > asd + 1:
                if self.altura_no(n.esq.dir) > self.altura_no(n.esq.esq):
                    return self.rotacao_dupla_dir(n)
                else:
                    return self.rotacao_dir(n)
            n.altura = self.altura_no(n)
        return n
