from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy
from enum import Enum, auto

class Categoria(Enum):
    REDE = auto()
    HARDWARE = auto()
    SOFTWARE = auto()
    SISTEMA = auto()

class Prioridade(Enum):
    ALTA = auto()
    MEDIA = auto()
    BAIXA = auto()

class Status(Enum):
    ABERTO = auto()
    ATENDIMENTO = auto()
    CONCLUIDO = auto()

@dataclass
class item:
    chave: int
    contido: lista | Chamado

class Chamado:
    def __init__(self, identificador:int, descricao:str, categoria:Categoria, prioridade:Prioridade, prazo:int, status:Status):
        self.identificador = identificador
        self.descricao = descricao
        self.categoria = categoria
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = status

class no:
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None 

class lista:
    def __init__(self):
        self.primeiro: no | None = None
        self.ultimo: no | None = None
    
    def vazia(self):
        return self.primeiro == None
    
    def busca(self, chave:int) -> no | None:
        ptr = self.primeiro
        while (ptr != None) and (ptr.dado.chave != chave):
            ptr = ptr.prox
        return ptr
    
    def busca_item(self, chave:int) -> item | None:
        ptr = self.busca(chave)
        if ptr != None:
            return deepcopy(ptr.dado)
        else:
            return None
    
    def insere_ini(self, x:item) -> bool:
        if self.busca(x.chave) == None:
            novo = no(x)
            if self.vazia():
                self.ultimo = novo
            novo.prox = self.primeiro
            self.primeiro = novo
            return True
        else:
            return False

    def insere_fim(self, x:item) -> bool:
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

    def procura_prazo(self, prazo:int)-> lista:
        posicao = prazo % self.capacidade
        if self.tabela[posicao].busca(prazo) != None:
            return self.tabela[posicao].busca(prazo).dado.contido
        else:
            return None
        
    def remover_prazo(self, prazo:int):
        posicao = prazo % self.capacidade
        if not(self.tabela[posicao].vazia()):
            self.tabela[posicao].remove_chave(prazo)

    def insere_chamado(self, chamado:Chamado):
        posicao = chamado.prazo % self.capacidade
        lista_altera = self.procura_prazo(chamado.prazo)
        if lista_altera == None:
            self.tabela[posicao].insere_fim(item(chamado.prazo,lista()))
        lista_altera = self.procura_prazo(chamado.prazo)
        lista_altera.insere_fim(item(chamado.identificador,chamado))

    def exclui_chamado(self, chamado:Chamado):
        posicao = chamado.prazo % self.capacidade
        lista = self.tabela[posicao].busca(chamado.prazo)
        if lista != None:
            lista.dado.contido.remove_chave(chamado.identificador)
            if lista.dado.contido.vazia():
                self.remover_prazo(chamado.prazo)
  

   

    