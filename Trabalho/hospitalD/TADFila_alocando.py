from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int | None
    tipo:  int 

class fila:
    def __init__(self):
        """
        Inicia a fila vazia com 10 de espaço de memória 
        """
        tam_max           = 10
        self.posicao: int = 0
        self.elementos: list[item] = [item(None,-1)] * tam_max
        self.tam_max      = tam_max
        self.fim          = 0    
    
    def vazia(self) -> bool:
        '''retorna True se a fila estiver vazia e False caso contrário
        Exemplos:
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        >>> f.vazia()
        False'''
        return self.fim == 0
    
    def cheia(self) -> bool:
        '''retorna True se a fila estiver cheia e False caso contrário
        Exemplos:
        >>> f = fila()
        >>> f.cheia()
        False
        >>> f.enfileira_geral()
        >>> f.cheia()
        False
        >>> f.enfileira_geral()
        >>> f.cheia()
        False'''
        return self.fim == self.tam_max
    
    def enfileira_geral(self):
        """
        Enfileira um elemento de forma normal, colocando no final da fila.
        Exemplos:
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        >>> f.vazia()
        False

        """
        if self.cheia():
            raise ValueError('Fila cheia')
        else:
            self.posicao += 1
            self.elementos[self.fim] = item(deepcopy(self.posicao),0)
            self.fim += 1


    def enfileira_prioritaria(self):
            """
            Enfileira um elemento com prioridade, ultrapassando elementos do tipo geral no máximo duas vezes.
            Exemplos:
            >>> f = fila()
            >>> f.vazia()
            True
            >>> f.enfileira_geral()
            >>> f.enfileira_geral() 
            >>> f.enfileira_prioritaria()
            >>> z = f.desenfileira()
            >>> print(z)
            3
            """
            if self.cheia():
                raise ValueError('Fila cheia')
            else:
                i = self.fim
                while i > 0 and (( self.elementos[i-1].tipo > -1 and self.elementos[i-1].tipo < 2) or self.elementos[i].valor == None):
                    if self.elementos[i-1].tipo  != -1:
                        self.elementos[i-1].tipo += 1
                    self.elementos[i] = self.elementos[i-1]
                    i-=1
                
                self.posicao += 1
                self.elementos[i] = item(deepcopy(self.posicao),-1)
                self.fim += 1
                
                

    def desenfileira(self):
        '''remove um elemento ao inicio da fila caso a 
        mesma não esteja vazia
        Exemplos:
        >>> f = fila()
        >>> f.enfileira_geral()
        >>> f.enfileira_geral()
        >>> x  = f.desenfileira()
        >>> print(x)
        1
        '''
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            retorno = self.elementos[0].valor
            for i in range(0,self.fim):
                self.elementos[i-1] = self.elementos[i]
            self.fim -= 1
            return retorno
