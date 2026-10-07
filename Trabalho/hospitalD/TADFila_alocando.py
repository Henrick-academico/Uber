from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int | None
    tipo:  int 

class fila:
    def __init__(self):
        tam_max           = 10
        self.posicao: int = 0
        self.elementos: list[item] = [item(None,-1)] * tam_max
        self.tam_max      = tam_max
        self.fim          = 0    
    
    def vazia(self) -> bool:
        '''retorna True se a fila estiver vazia e False caso contrário
        Exemplos:
        >>> f = fila(5)
        >>> f.vazia()
        True
        >>> f.enfileira(item(2))
        >>> f.vazia()
        False'''
        return self.fim == 0
    
    def cheia(self) -> bool:
        '''retorna True se a fila estiver cheia e False caso contrário
        Exemplos:
        >>> f = fila(2)
        >>> f.cheia()
        False
        >>> f.enfileira(item(2))
        >>> f.cheia()
        False
        >>> f.enfileira(item(1))
        >>> f.cheia()
        True'''
        return self.fim == self.tam_max
    
    def enfileira_geral(self):
        
        if self.cheia():
            raise ValueError('Fila cheia')
        else:
            self.posicao += 1
            self.elementos[self.fim] = item(deepcopy(self.posicao),0)
            self.fim += 1

    def enfileira_prioritaria(self):
            if self.cheia():
                raise ValueError('Fila cheia')
            else:
                i = self.fim
                while i > 0 and (( self.elementos[i].tipo > -1 and self.elementos[i].tipo < 2) or self.elementos[i].valor == None):
                    if self.elementos[i].tipo  != -1:
                        self.elementos[i].tipo += 1
                    self.elementos[i-1] = self.elementos[i]
                    i-=1
                    
                self.posicao += 1
                self.elementos[i] = item(deepcopy(self.posicao),-1)
                self.fim += 1
                
                

    def desenfileira(self):
        '''remove um elemento ao inicio da fila caso a 
        mesma não esteja vazia
        Exemplos:
        >>> f = fila(2)
        >>> f.enfileira(item(2))
        >>> f.enfileira(item(3))
        >>> f.desenfileira()
        >>> x: int = f.obtem_primeiro().valor
        >>> x
        3'''
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            retorno = self.elementos[0].valor
            for i in range(1,self.fim):
                self.elementos[i-1] = self.elementos[i]
            self.fim -= 1
            return retorno
    

