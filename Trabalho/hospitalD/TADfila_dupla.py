from dataclasses import *

@dataclass
class item:
    valor:int | None 

class no:
    """
    Permite criar filas apontando seu próximo e seu anterior alem de guardar um valor do tipo item, o dado tipo ajuda a definir quais nós são do tipo geral bem como quantos prioritarios o passaram
    """
    def __init__(self,x: item):
        self.tipo: int  = -1
        self.dado: item = x
        self.prox: no | None = None
        self.ant:  no | None = None

class fila:
    def __init__(self):
        """
        Inicia a fila criando um nó sentinela, uma variavel de posição para cada novo nó, um ponteiro para o primeiro e um para o ultimo nó.
        """
        self.posicao: int = 0
        self.primeiro = no(item(None))
        self.ultimo   = self.primeiro
        self.primeiro.prox = None
        self.primeiro.ant  = None

    def vazia(self) -> bool:
        """
        Verifica se uma fila está vazia.
        Exemplo:
        >>> f = fila()
        >>> f.enfileira_geral()
        >>> f.vazia()
        False
        >>> f.desenfileira()
        1
        >>> f.vazia()
        True
        """
        return self.primeiro.prox == None

    def enfileira_geral(self):
        """
        Coloca um novo valor na fila
        Exemplo:
        >>> f = fila()
        >>> f.vazia()
        True
        >>> f.enfileira_geral()
        >>> f.vazia()
        False
        """
        self.posicao += 1
        novo             = no(self.posicao)
        novo.tipo        = 0
        self.ultimo.prox = novo
        novo.ant         = self.ultimo
        self.ultimo      = novo

    def enfileira_prioritaria(self):
        """
        Coloca em uma posição prioritaria ultrapassando posições gerais que estavam na fila no máximo duas vezes.
        Exemplo:
        >>> f = fila()
        >>> f.enfileira_geral()
        >>> f.enfileira_prioritaria()
        >>> z = f.desenfileira()
        >>> print(z)
        2
        >>> z = f.desenfileira()
        >>> print(z)
        1

        """
        self.posicao += 1
        novo    = no(self.posicao)
        aux: no = self.ultimo

        while aux != self.primeiro and aux.tipo>-1 and aux.tipo<2:
            if aux.tipo != -1:
                aux.tipo += 1
            aux = aux.ant
        novo.ant = aux
        
        if aux.prox != None:
            aux.prox.ant = novo
            novo.prox    = aux.prox
        else:
            self.ultimo = novo
        aux.prox = novo
    
    def desenfileira(self)->item:
        """
        Retira o valor que estiver em primeiro na fila
        Exemplo:
        >>> f = fila()
        >>> f.enfileira_geral()
        >>> f.enfileira_prioritaria()
        >>> z = f.desenfileira()
        >>> print(z)
        2
        >>> z = f.desenfileira()
        >>> print(z)
        1
        """
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            rem = self.primeiro.prox
            self.primeiro.prox = rem.prox

            if rem.prox != None:
                rem.prox.ant = self.primeiro
                rem.prox     = None
            else:
                self.ultimo = self.primeiro
            rem.ant = None

            return rem.dado
            




        
       
        

    
    
