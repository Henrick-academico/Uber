from dataclasses import dataclass
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
    

def main():
    repetir = True
    identificador = 100
    while repetir:
        
        opcao = int(input("Selecione uma opção:\n 1.Abrir chamado \n 2.Consultar chamados por prazo \n 3.Consultar chamado por ID e prazo \n 4.Alterar dados de um chamado \n 5.Excluir um chamado \n 6.Listar todos os chamados \n 7.Encerrar o programa \n"))
        if opcao == 1:
            identificador+=1
            descricao = input("Descreva o problema: ")
            categoria = int(input("Selecione a categoria do chamado: \n 1.Rede \n 2.Hardware \n 3.Software \n 4.Sistema institucional \n"))
            prioridade = int(input("Selecione a prioridade do chamado: \n 1.Alta \n 2.Média \n 3.Baixa \n "))
            prazo = int(input("Prazo de atendimento em horas: "))
            categoria = int(input("Selecione o status do chamado: \n 1.Aberto \n 2.Em atendimento \n 3.Concluído \n"))


        elif opcao == 7:
            repetir = False
        else:
            print("Informe um valor valido")







main()
