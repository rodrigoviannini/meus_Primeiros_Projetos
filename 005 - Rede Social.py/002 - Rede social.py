# IMPORTO O CSV PARA ABRIR E LER OS ARQUIVOS CSV.
import csv

# CLASSE: PERFIL -> Construindo o objeto chamado PERFIL"""
class Perfil(object):
    
    def __init__(self): 
        self.adjacencia ={}
        """ FUNCAO __INIT__: CONSTRUTOR (PARÂMETRO): 
            Adjacencias -> Instanciam as classes """

    # FUNCAO: ADCIONA
    def adiciona(self, vertice):      # Pega o vértice coletado na função COLETA VERTICE CSV
        self.adjacencia[vertice] = {}   # adciona no dicionário
        """ FUNCAO ADCIONA: 
            Recebe o nome da pessoa (vértice) e coloca no dicionário
            Recebe de quem? De outra função que coleta os dados """
  
    # FUNCAO: COLETA individuoQualquer CSV
    def coletaUsuarioCSV (self, individuoQualquer):        # ABASTECE A MATRIZ ADJACENCIA (todas as KEYS da matriz ADJACENCIA)
        """ FUNÇÃO QUE ABRE E LÊ O ARQUIVO CSV
            COLETA VERTICE DO ARQUIVO DE USUÁRIOS
            CHAMA O MÉTODO ADCIONA DENTRO DELE MESMO (passa no arquivo coleta o nome e adciona no meu grafo)"""
        with open(individuoQualquer, newline='') as u_csv:     # Abre o arquivo
            leitura = csv.reader(u_csv)                        # Lê
            for linha in leitura:                              # Para linha na leitura do arquivo
                self.adiciona(linha[1])                        # Chamo a função adiciona que...
   

    # FUNCAO: CONECTAR
    def conecta(self, individuo_1, individuo_2, peso):
        self.adjacencia[individuo_1][individuo_2] = peso  # Conecto os indivíduos de acordo com o peso 1 e 2
    
    # FUNCAO: COLETA CONEXOES
    def coletaConexoesCSV (self, conexoes):                 # ABASTECE A MATRIZ ADJACENCIA
        """ FUNÇÃO QUR ABRIR E LER O ARQUIVO CSV
        COLETA CONEXOES -> PEGA O ARQUIVO DE CONEXOES
        CHAMA O MÉTODO CONECTA DENTRO DELE MESMO (passa no arquivo coleta o nome e adciona no meu grafo) """ 
        with open(conexoes, newline='') as c_csv:             # Abre o arquivo
            leitura = csv.reader(c_csv)                         # Lê
            for linha in leitura:                               # Para linha na leitura do arquivo
                self.conecta(linha[0], linha[1], linha[2])        # Chamo a função conecta individuo 1, 2 e Peso, que...

    # FUNCAO: EXIBIR SEGUIDORES
    def exibeSeguidores (self, individuoQualquer):
        """ FUNCAO QUE EXIBE QUE SEGUE O INDIVIDUO
            DEVE-SE VARRER O DICIONARIO DO DICIONARIO PARA SABER QUANTAS PESSOAS SE CONECTARAM COM UM INDIVIDUO ESPECÍFICO, OU SEJA, 
            QUANTAS SETINHAS CHEGAM NESTE VÉRTICE """

        seguidores = []                             # Crio uma lista vazia para receber os seguidores do append
        for linha in self.adjacencia.items():       # Para cada linha dentro da minha matriz faço uma nova varredura, segue abaixo:
            for itemLinha in linha[1].items():        # Para cada itemLinha contido no index 1 desta linha:
                if individuoQualquer in itemLinha:      # Se o individuo esta contido/ conectado no itemLinha, faço:
                    seguidores.append(linha[0])           # Pego o indivíduo coloco ele dentro da lista de seguidores no index 0 da linha 
        
        print(f'O login {individuoQualquer} possui {len(seguidores)} seguidores.')

    #  FUNCAO: EXIBIR SEGUIDOS
    def exibeSeguidos(self, individuoQualquer):                           # Pego o usuario (chave principal), quantas pessoas ele segue? (qtas conexoes)
        """ FUNCAO QUE EXIBE QUEM O INDIVÍDUO SEGUE """
        seguidos = len(self.adjacencia[individuoQualquer].keys())           # Quantas keys? - Pego o valor da chave do individuo dentro da matriz e contabilizo e salvo dentro da variavel SEGUIDOS

        print(f'O login {individuoQualquer} segue {seguidos} pessoas.')

    # FUNCAO: MELHORES AMIGOS
    def melhoresAmigos(self, individuoQualquer):

        listaAmigos = list(self.adjacencia[individuoQualquer].items())     # Vou varrer o ADJACENCIA e transformar em uma lista de ITEMS

        listaAmigosComuns = []                                             # Crio uma lista vazia para separar os amigos comuns
        listaMelhoresAmigos = []                                           # Crio uma lista vazia para separar os amigos comuns

        for item in listaAmigos:                                           # Para cada item dentro da lista que eu varrI
            if item[1] == '2':                                               # Se o item tiver peso 2, coloco na lista melhores amigos
                listaMelhoresAmigos.append(item[0])
            elif item[1] == '1':
                listaAmigosComuns.append(item[0])                              # Se o item tiver peso 1, coloco na lista amigos comuns
    
        # MERGESORT
        def juntar_lista(self, listaAmigosComuns, listaMelhoresAmigos):                                   # lista comuns e melhores -> Refere-se a metade da esquerda e da direita
            lista_retorno = [None] * (len(listaAmigosComuns) + len(listaMelhoresAmigo))                     # Lista que iremos retornar no final
            cursor_lista_comuns = 0                                                                         # cursor_lista_comuns começa no index zero
            cursor_lista_melhores = 0                                                                       # cursor_lista_melhores começa no index zero
            ''' Criamos estas variaveis dos cursores pois iremos utilizá-las de maneira assíncrona '''
        
            for i in range(len(lista_retorno)):                                                             # Estamos pegando os indices do tamanho da lista retorno
                if cursor_lista_comuns >= len(listaAmigosComuns):                                           # Se estourar a lista comuns
                    lista_retorno[i] = listaMelhoresAmigos[cursor_lista_melhores]                           # A lista retorno no index atual vai receber o 'cursor 2' onde ele esta localizado
                    cursor_lista_melhores += 1                                                              # Anda uma casa
            
                elif cursor_lista_melhores >= len(listaMelhoresAmigos):                                     # mesma coisa do IF, porem ao contrario!
                    lista_retorno[i] = listaAmigosComuns[cursor_lista_comuns] 
                    cursor_lista_comuns += 1
            
                elif listaAmigosComuns[cursor_lista_comuns] <= listaMelhoresAmigos[cursor_lista_melhores]:  # Como descobrir qual dos elementos é menor?
                    lista_retorno[i] = listaAmigosComuns[cursor_lista_comuns]                               # Vou inserir o menor 'elemnto da lista 1)
                    cursor_lista_comuns += 1                                                                # Atualizo meu cursor, ando uma casa!
            
                elif listaMelhoresAmigos[cursor_lista_melhores] < listaAmigosComuns[cursor_lista_comuns]:   # mesma coisa do ELIF anterior, porem ao contrario!
                    lista_retorno[i] = listaMelhoresAmigos[cursor_lista_melhores]
                    cursor_lista_melhores += 1
                
            return lista_retorno

        def dividir(listaAmigos):                                           
            if len(listaAmigos) <= 1:                                                             # Quando o numero de elementos da minha lista for igaul a 1
            
            #return listaAmigos   ERRRO FDP                                                     # Retorno a lista, ou seja, o elemento solitario 
        
                meio = len(listaAmigos) // 2                                                        # Acho o meio da lista
                
                listaAmigosComuns = listaAmigos[:meio]                                              # do zero até o meio
                
                listaMelhoresAmigos = listaAmigos[meio:]                                            # do meio até o final
            
                resultado_divisao_comuns = dividir(listaAmigosComuns)                               # chamo a função 'dividir comuns e armazeno em uma variável

                resultado_divisao_melhores = dividir(listaMelhoresAmigos)                           # chamo a função 'dividir melhores' e armazeno em uma variável  
                    
                return juntar_lista(resultado_divisao_comuns + resultado_divisao_melhores)
                
        print(f"A ordem de amigos que irão receber as publicações de {individuoQualquer} primeiro é: {juntar_lista}.")


    # FUNCAO: TOP K INFLUENCIADORES
        def topKInfluenciadores(self, k):
            ''' Encontrar os individuos que são mais seguidos (Preciso saber o numero 
            máximo de seguidores de cada individuo)'''

            dicionarioKInfluenciadores = {}                                                  # Dicionario com numero de seguidores para cada vértice

            for individuoQualquer in self.adjacencia:
                influenciadores = 0                                                            # Preciso de um contador para poder somar
                for linha in self.adjacencia.items():
                    for item in linha[1].items():
                        if individuoQualquer in item:
                            influenciadores +=1
                dicionarioKInfluenciadores[individuoQualquer] = influenciadores

            listaComInflenciadores = list(dicionarioKInfluenciadores.items())
        
        # ORGANIZANDO MINHA LISTA 
            for x in range(len(listaComInflenciadores)):
                for y in range(len(listaComInflenciadores)):
                    if listaComInflenciadores[y][1] < listaComInflenciadores[x][1]:
                        listaComInflenciadores[x], listaComInflenciadores[y] = listaComInflenciadores[y], listaComInflenciadores[x]

            ranking = ''                                                                      # Faço uma iteração para transformar em string com nome do individuo e qtde de seguidores
            for item in listaComInflenciadores[:k]:
                ranking += str(item[0]) + ', com ' + str(item[1]) + " influenciadores; "
        
            return print(f"Os {k} influenciadores que se destacam com mais seguidores são: {ranking[:-2]}.")


    # FUNCAO: EXIBE CAMINHOS DO INDIVIDUO
    
        def exibeCaminhoIndividuo (self, individuo_1, individuo_2): # Desafio da aula 8
            fila = [individuo_1]
            visitados = []
            predecessor = {individuo_1: None}
        
            while len(fila) > 0:
                primeiro_elemento = fila[0]
                fila = fila[1:]
                visitados.append(primeiro_elemento)

            for adjacente in self.adjacencia[primeiro_elemento].keys():       
                
                if adjacente == individuo_2:
                    pred = primeiro_elemento
                    caminho_invertido = [individuo_2]

                    while pred is not None:
                        caminho_invertido.append(pred)
                        pred = predecessor[pred]
                        
                    caminho = ''
                    for no in caminho_invertido[::-1]:
                        caminho += f'{no} -> '
                    return print(f"O caminho de inter-relacionamento entre os indivíduos é :{caminho[:-3]}")
                
                if adjacente not in fila and adjacente not in visitados:
                    predecessor[adjacente] = primeiro_elemento
                    fila.append(adjacente)
            return False 
        

  
# RESULTADOS
p = Perfil()
p.coletaUsuarioCSV('usuarios.csv')
p.coletaConexoesCSV('conexoes.csv')
p.exibeSeguidores('helena42')
print()
p.exibeSeguidos('helena42')
print()
p.melhoresAmigos('helena42')
print()
p.topKInfluenciadores(5)
print()
p.exibeCaminhoIndividuo('helena42', 'valentina26')
