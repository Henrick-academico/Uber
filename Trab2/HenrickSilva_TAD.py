from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy
from enum import Enum, auto

class Categoria(Enum):
    ''' 
    Representa o tipo de problema de Chamado
    '''
    REDE = auto()
    HARDWARE = auto()
    SOFTWARE = auto()
    SISTEMA = auto()

class Prioridade(Enum):
    ''' 
    Representa o nível de prioridade de Chamado
    '''
    ALTA = auto()
    MEDIA = auto()
    BAIXA = auto()

class Status(Enum):
    ''' 
    Representa a situação de Chamado
    '''
    ABERTO = auto()
    ATENDIMENTO = auto()
    CONCLUIDO = auto()

@dataclass
class item:
    '''
    guarda uma chave para procurar o item e uma variavel que pode ser uma lista ou um chamado
    '''
    chave: int
    contido: lista | Chamado

class Chamado:
    '''
    guarda as especificações de um chamado
    '''
    def __init__(self, identificador:int, descricao:str, categoria:Categoria, prioridade:Prioridade, prazo:int, status:Status):
        self.identificador = identificador
        self.descricao = descricao
        self.categoria = categoria
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = status

class no:
    '''
    guarda um nó que ajuda a montar a fila.
    '''
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None 

class lista:
    def __init__(self):
        self.primeiro: no | None = None
        self.ultimo: no | None = None
    
    def vazia(self):
        '''
        Verifica se a lista está vazia.
        Retorna True caso o primeiro elemento da lista seja None. Caso contrário, retorna False.

        Exemplo:
        >>> lista = Lista()
        >>> lista.vazia()
        True
        '''
        return self.primeiro == None
    
    def busca(self, chave:int) -> no | None:
        '''
        Busca um elemento na lista a partir de sua chave.
        Percorre a lista até encontrar um elemento com a chave informada. Caso encontre, retorna o nó correspondente. Caso contrário, retorna None.
        Exemplo:
        >>> lista = lista()
        >>> lista.insere_fim(item(101,chamado()))
        >>> no  = lista.busca(101)
        >>> print(no.dado.chave)
        101

        '''
        ptr = self.primeiro
        while (ptr != None) and (ptr.dado.chave != chave):
            ptr = ptr.prox
        return ptr
    
    def busca_item(self, chave:int) -> item | None:
        '''
        Busca um elemento na lista a partir de sua chave.
        Percorre a lista até encontrar um elemento com a chave informada. Caso encontre, retorna uma cópia do nó correspondente. Caso contrário, retorna None.
        Exemplo:
        >>> lista = lista()
        >>> lista.insere_fim(item(101,chamado()))
        >>> no  = lista.busca(101)
        >>> print(no.dado.chave)
        101
        '''
        ptr = self.busca(chave)
        if ptr != None:
            return deepcopy(ptr.dado)
        else:
            return None
    
    def insere_fim(self, x:item) -> bool:
        '''
        Insere um novo elemento no final da lista.
        Verifica se já existe um elemento com a mesma chave. Caso não exista, cria um novo nó e o adiciona ao final da lista. Retorna True se a inserção for realizada ou False caso a chave já exista.
        Exemplo:
        >>> item1 = item(101,Chamado())
        >>> lista = lista()
        >>> lista.insere_ini(item1)
        >>> lista.insere_fim(item1)
        True
        >>> lista.insere_fim(item1)
        False
        
        '''
        if self.busca(x.chave) == None:
            novo = no(x)
            if self.vazia():
                self.primeiro = novo
            else:
                self.ultimo.prox = novo
            novo.prox = None
            self.ultimo = novo
            return True
        else:
            return False

    def remove_chave(self, chave: int) -> bool:
        '''
        Remove um elemento da lista a partir de sua chave.
        Percorre a lista procurando o elemento com a chave informada. Caso encontre, remove o nó correspondente e ajusta os ponteiros da lista. Retorna True se a remoção for realizada ou False caso a chave não seja encontrada ou a lista esteja vazia.

        Exemplo:
        >>> item1 = item(101,Chamado())
        >>> lista = lista()
        >>> lista.insere_ini(item1)
        >>> lista.remove_chave(101)
        True
        >>> lista.remove_chave(999)
        False
        '''
        ptr = self.primeiro
        if not self.vazia():
            if ptr.dado.chave == chave:
                return self.remove_ini()
            while ptr.prox != None and ptr.prox.dado.chave != chave:
                ptr=ptr.prox
            if ptr.prox != None:
                exc = ptr.prox
                ptr.prox = exc.prox
                if ptr.prox == None:
                    self.ultimo = ptr
                exc.prox = None
                return True
        return False
    
    def remove_ini(self):
        '''
        Remove o primeiro elemento da lista.
        Verifica se a lista não está vazia, remove o primeiro nó e atualiza o ponteiro para o próximo elemento. Caso a lista fique vazia após a remoção, o ponteiro do último elemento também é definido como None. Retorna o dado armazenado no nó removido.

        Exemplo:
        >>> item1 = item(101,Chamado())
        >>> item2 = item(102,Chamado())
        >>> lista = lista()
        >>> lista.insere_ini(item1)
        >>> lista.insere_ini(item2)
        >>> lista.remove_ini()
        item2
        '''
        if not self.vazia():
            rem = self.primeiro
            self.primeiro = self.primeiro.prox
            if self.vazia():
                self.ultimo = None
            rem.prox = None
            return rem.dado

##################################

class tabelahash:
    def __init__ (self, capacidade: int):
        self.capacidade = capacidade
        self.tabela = [lista() for _ in range(capacidade)]

    def procura_prazo(self, prazo:int)-> lista | None:
        '''
        Procura um elemento na tabela hash utilizando o prazo como chave.
        Calcula a posição na tabela através do resto da divisão do prazo pela capacidade. Em seguida, busca o elemento na lista correspondente à posição calculada. Caso encontre, retorna o conteúdo armazenado no elemento. Caso contrário, retorna None.
        Exemplo:
        >>> tabela.procura_prazo(20)
        lista_encontrada
        >>> tabela.procura_prazo(999)
        None
        '''
        posicao = prazo % self.capacidade
        if self.tabela[posicao].busca(prazo) != None:
            return self.tabela[posicao].busca(prazo).dado.contido
        else:
            return None
    
        
    def remover_prazo(self, prazo:int):
        '''
        Remove um elemento da tabela hash utilizando o prazo como chave.
        Calcula a posição na tabela através do resto da divisão do prazo pela capacidade. Verifica se a lista correspondente à posição não está vazia e, caso não esteja, remove o elemento que possui a chave igual ao prazo informado.

        Exemplo:
        >>> tabela.remover_prazo(20)
        '''
        posicao = prazo % self.capacidade
        if not(self.tabela[posicao].vazia()):
            self.tabela[posicao].remove_chave(prazo)

    def insere_chamado(self, chamado:Chamado):
        '''
        Insere um chamado na tabela hash utilizando o prazo como chave.
        Calcula a posição na tabela através do resto da divisão do prazo pela capacidade. Verifica se já existe uma lista associada ao prazo. Caso não exista, cria uma nova lista e a insere na posição correspondente. Em seguida, adiciona o chamado à lista encontrada, utilizando seu identificador como chave.
        Exemplo:
        >>> tabela.insere_chamado(chamado1)
                
        '''
        posicao = chamado.prazo % self.capacidade
        lista_altera = self.procura_prazo(chamado.prazo)
        if lista_altera == None:
            self.tabela[posicao].insere_fim(item(chamado.prazo,lista()))
        lista_altera = self.procura_prazo(chamado.prazo)
        lista_altera.insere_fim(item(chamado.identificador,chamado))

    def exclui_chamado(self, chamado:Chamado):
        '''
        Exclui um chamado da tabela hash utilizando seu prazo e identificador.
        Calcula a posição na tabela através do resto da divisão do prazo pela capacidade. Busca a lista correspondente ao prazo informado e, caso encontre, remove o chamado utilizando seu identificador. Se a lista ficar vazia após a remoção, remove também o prazo correspondente da tabela hash.
        Exemplo:
        >>> tabela.exclui_chamado(chamado1)
        '''
        posicao = chamado.prazo % self.capacidade
        lista = self.tabela[posicao].busca(chamado.prazo)
        if lista != None:
            lista.dado.contido.remove_chave(chamado.identificador)
            if lista.dado.contido.vazia():
                self.remover_prazo(chamado.prazo)

    def vazia(self) -> bool:
        '''
        Verifica se a tabela hash está vazia.
        Percorre todas as posições da tabela e verifica se existe alguma lista com elementos. Caso encontre alguma lista não vazia, retorna False. Se todas as listas estiverem vazias, retorna True.
        Exemplo:
        >>> tabela.vazia()
        True
        '''
        for prazos in self.tabela:
            if not(prazos.vazia()):
                return False
        return True

   

    