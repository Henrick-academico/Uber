from dataclasses import dataclass
from HenrickSilva_TAD import *


def main():
    repetir = True
    identificador = 100
    tabela_hash = tabelahash(5)
    while repetir:
        
        opcao = int(input("Selecione uma opção:\n 1.Abrir chamado \n 2.Consultar chamados por prazo \n 3.Consultar chamado por ID e prazo \n 4.Alterar dados de um chamado \n 5.Excluir um chamado \n 6.Listar todos os chamados \n 7.Encerrar o programa \n"))
        match opcao:
            case 1:
                identificador+=1
                print("ID do chamado:",identificador)
                descricao = input("Descreva o problema: ")
                categoria = int(input("Selecione a categoria do chamado: \n 1.Rede \n 2.Hardware \n 3.Software \n 4.Sistema institucional \n"))
                prioridade = int(input("Selecione a prioridade do chamado: \n 1.Alta \n 2.Média \n 3.Baixa \n "))
                prazo = int(input("Prazo de atendimento em horas: "))
                status= int(input("Selecione o status do chamado: \n 1.Aberto \n 2.Em atendimento \n 3.Concluído \n"))
                match categoria:
                    case 1:
                        categoria_tipo = Categoria.REDE
                    case 2:
                        categoria_tipo = Categoria.HARDWARE
                    case 3:
                        categoria_tipo = Categoria.SOFTWARE
                    case 4:
                        categoria_tipo = Categoria.SISTEMA
                match prioridade:
                    case 1:
                        prioridade_tipo = Prioridade.ALTA
                    case 2:
                        prioridade_tipo = Prioridade.MEDIA
                    case 3:
                        prioridade_tipo = Prioridade.BAIXA
                match status:
                    case 1:
                        status_tipo = Status.ABERTO
                    case 2:
                        status_tipo = Status.ATENDIMENTO
                    case 3:
                        status_tipo = Status.CONCLUIDO
                
                chamado = Chamado(identificador,descricao,categoria_tipo,prioridade_tipo,prazo,status_tipo)
                tabela_hash.insere_chamado(chamado)
            case 2:
                prazo = int(input("Digite o Prazo que deseja consultar: "))

            case 3:
                prazo = int(input("Digite o Prazo que deseja consultar: "))
                identificador_procura = int(input("Digite o ID que deseja consultar: "))

            case 4:
                prazo = int(input("Digite o Prazo que deseja alterar: "))
                identificador_procura = int(input("Digite o ID que deseja alterar: "))

            case 5:
                prazo = int(input("Digite o Prazo que deseja excluir: "))
                identificador_procura = int(input("Digite o ID que deseja excluir: "))
            case 6:
                print("listar chamados")
            
            case 7:
                repetir = False
            case _:
                print("Informe um valor valido")







main()