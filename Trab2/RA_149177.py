from HenrickSilva_TAD import *
from copy import deepcopy

def valida(limite: int, texto:str)-> int:
    '''
    Valida se uma entrada está dentro do *limite* e em formato int, *texto* é a pergunta para receber a entrada
    Exemplo:
    >>> valida(200, "digite um número:")
    digite um número:
    300
    digite um valor valido
    digite um número:
    trinta e dois
    digite um valor valido
    digite um número:
    32
    '''
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
    '''
    Imprime todas as informações de *chamado* formatado
    Exemplo:
    >>> chamado1 = Chamado(101,"problema1", Categoria.REDE, Prioridade.ALTA, 20, Status.ABERTO)
    >>> chamado2 = Chamado(102,"problema2", Categoria.HARDWARE, Prioridade.MEDIA, 10, Status.ATENDIMENTO)
    >>> chamado3 = Chamado(103,"problema3", Categoria.SISTEMA, Prioridade.BAIXA, 8, Status.CONCLUIDO)
    >>> imprime_chamado(chamado1)
    ID: 101
    Descrição: problema1
    Categoria: REDE
    Prioridade: ALTA
    Status: ABERTO
    >>> imprime_chamado(chamado1)
    ID: 102
    Descrição: problema2
    Categoria: HARDWARE
    Prioridade: MEDIA
    Status: ATENDIMENTO

    >>> imprime_chamado(chamado1)
    ID: 103
    Descrição: problema3
    Categoria: SISTEMA
    Prioridade: BAIXA
    Status: CONCLUIDO

    '''
    print("ID:",chamado.identificador)
    print("Descrição:",chamado.descricao)
    print("Categoria:",chamado.categoria.name)
    print("Prioridade:",chamado.prioridade.name)
    print("Status:",chamado.status.name)
    print()

def valida_existencia(tabela_hash: tabelahash ,verbo:str)-> Chamado | None:
        '''
        Valida a existemxia de um chamado na *tabela_hash, e usa verbo para perguntar sobre o tipo de alteração que será feita.
        Exemplo:
        >>> tabela = tabelahash()
        >>> chamado1 = Chamado(101,"problema1", Categoria.REDE, Prioridade.ALTA, 20, Status.ABERTO)
        >>> tabela.insere_chamado(chamado1)
        >>> valida_existencia(tabela,"procurar")
        Digite o Prazo que deseja procurar:20
        Digite o ID que deseja procurar:200
        Não há chamados com esse ID
        >>> chamado = valida_existencia(tabela,"procurar")
        Digite o Prazo que deseja procurar:20
        Digite o ID que deseja procurar:101
        >>> imprime_chamado(chamado1)
        ID: 101
        Descrição: problema1
        Categoria: REDE
        Prioridade: ALTA
        Status: ABERTO
        
        '''
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
    '''
    Preenche todos os valores necessários e cria um chamado usando *identificador* como ID.
    Exemplo:
    >>> chamado = preecher_chamado(101)
    Descreva o problema: Rede não conecta
    Selecione a categoria do chamado: 
    1.Rede 
    2.Hardware 
    3.Software 
    4.Sistema institucional 
    1
    Selecione a prioridade do chamado: 
    1.Alta 
    2.Média 
    3.Baixa 
    1
    Prazo de atendimento em horas: 1
    Selecione o status do chamado: 
    1.Aberto 
    2.Em atendimento 
    3.Concluído 
    1
    >>> imprime_chamado(chamado1)
    ID: 101
    Descrição: Rede não conecta
    Categoria: REDE
    Prioridade: ALTA
    Status: ABERTO

    '''
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
                    tabela_hash.exclui_chamado(chamado_alterar)
                    tabela_hash.insere_chamado(chamado)
                    
            case 5:
                chamado_excluir = valida_existencia(tabela_hash,"excluir")
                if chamado_excluir != None:
                    tabela_hash.exclui_chamado(chamado_excluir)

            case 6:
                tabela_exibir = deepcopy(tabela_hash)
                i = 0
                
                while not(tabela_exibir.vazia()) and i < tabela_exibir.capacidade:
                    lista_prazos = tabela_exibir.tabela[i]
                    while not(lista_prazos.vazia()):
                        prazo_exibir = lista_prazos.primeiro.dado.contido
                        while not(prazo_exibir.vazia()):
                            chamado_exibir = prazo_exibir.primeiro.dado.contido
                            imprime_chamado(chamado_exibir)
                            prazo_exibir.remove_ini()
                        lista_prazos.remove_ini()
                    i+=1

            case 7:
                repetir = False
            case _:
                print("Informe um valor valido")


main()