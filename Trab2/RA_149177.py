from dataclasses import dataclass
from HenrickSilva_TAD import *

def valida(limite: int, texto:str)-> int:
    variavel = 0
    while 0 >= variavel or variavel >= limite:
        try:
            variavel = int(input(texto))
        except ValueError:
            variavel = 0
        if 0 >= variavel or variavel >= limite:
            print("digite um valor valido")
    return variavel

def imprime_chamado(chamado:Chamado):
    print("ID:",chamado.identificador)
    print("Descrição:",chamado.descricao)
    print("Categoria:",chamado.categoria.value)
    print("Prioridade:",chamado.prioridade.value)
    print("Status:",chamado.status.value)
    print()

def valida_existencia(tabela_hash: tabelahash ,verbo:str)-> Chamado | None:
        prazo = int(input(f"Digite o Prazo que deseja {verbo}:"))
        lista_prazo = deepcopy(tabela_hash.procura_prazo(prazo))
        if lista_prazo == None:
            print("Não há chamados neste prazo \n")   
            return None   
        else:
            identificador_procura = int(input(f"Digite o ID que deseja {verbo}:"))
            chamado_consulta = lista_prazo.busca_item(identificador_procura)
            if chamado_consulta == None:
                print("Não há chamados com esse ID")
                return None  
        return chamado_consulta.contido

def preencher_chamado(identificador:int)->Chamado:
    descricao       = input("Descreva o problema: ")
    categoria       = valida(5,"Selecione a categoria do chamado: \n 1.Rede \n 2.Hardware \n 3.Software \n 4.Sistema institucional \n")
    categoria_tipo  = Categoria(categoria)
    prioridade      = valida(4,"Selecione a prioridade do chamado: \n 1.Alta \n 2.Média \n 3.Baixa \n ")
    prioridade_tipo = Prioridade(prioridade)
    prazo           = int(input("Prazo de atendimento em horas: "))
    status          = valida(4,"Selecione o status do chamado: \n 1.Aberto \n 2.Em atendimento \n 3.Concluído \n")
    status_tipo     = Status(status)          
    return Chamado(identificador,descricao,categoria_tipo,prioridade_tipo,prazo,status_tipo)


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
                chamado = preencher_chamado(identificador)
                tabela_hash.insere_chamado(chamado)

            case 2:
                prazo = int(input("Digite o Prazo que deseja consultar: "))
                lista_prazo = deepcopy(tabela_hash.procura_prazo(prazo))
                print("Chamados de", prazo,"Hrs de prazo")
                if lista_prazo == None:
                    print("Não há chamados neste prazo \n")
                while lista_prazo!=None and not(lista_prazo.vazia()):
                    chamado_prazo = lista_prazo.remove_ini()
                    imprime_chamado(chamado_prazo.contido)

            case 3:
                chamado_consulta = valida_existencia(tabela_hash, "consultar")
                if chamado_consulta != None:
                    imprime_chamado(chamado_consulta)

            case 4:
                chamado_alterar = valida_existencia(tabela_hash,"alterar")
                if chamado_alterar != None:
                    print("Atuais valores do chamado")
                    imprime_chamado(chamado_alterar)
                    print("\n Novos valores para o chamado")
                    chamado = preencher_chamado(chamado_alterar.identificador)
                    lista_alterar = tabela_hash.procura_prazo(chamado_alterar.prazo)
                    lista_alterar.remove_chave(chamado_alterar.identificador)
                    tabela_hash.insere_chamado(chamado)
                    if lista_alterar.vazia():
                        tabela_hash.remover_prazo(chamado_alterar.prazo)
            case 5:
                prazo = int(input("Digite o chamado que deseja excluir: "))
                identificador_procura = int(input("Digite o ID que deseja excluir: "))
            case 6:
                print("listar chamados")
            
            case 7:
                repetir = False
            case _:
                print("Informe um valor valido")







main()

main()