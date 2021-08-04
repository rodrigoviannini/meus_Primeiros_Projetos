"""

    ~ JOGO DA FORCA ~
    Author.: @rodrigoviannini

    OBS.: Meu primeiro projeto em Python, além de ser a primeira versão, visto que tenho exatos 1 Mês e 19 dias como programador! Estou feliz com o resultado, mas nunca satisfeito!

    Alterações para versão 2.

    1. Substituir funções globais por parametrizadas
    2. Substituir o hífen inputado pelo usuário por espaços em branco em palavras compostas
    3. Realizar melhorias

"""

# Primeiramente iremos utilizar as brechas do Python para criar uma seleção "pseudo-aleatória" usando o random
import random 


# Criação de lista do esboço da figura do enforcado
figuraForca = [
    '''
    +---+
    |   |
    |
    |
    |
    |
    =======''', """
    
    +---+
    |   |
    |   O
    |
    |
    |
    =======""","""
    
    +---+
    |   |
    |   O
    |   |   
    |   |
    |
    =======""","""
    
    +---+
    |   |
    |   O
    |  \|   
    |   |
    |
    =======""","""
    
    +---+
    |   |
    |   O
    |  \|/   
    |   |
    |
    =======""","""
    
    +---+
    |   |
    |   O
    |  \|/   
    |   |
    |  /
    =======""","""
    
    +---+
    |   |
    |   O
    |  \|/   
    |   |
    |  / \\
    ======="""
    ]


"""print(figuraForca[0])
print(figuraForca[1])
print(figuraForca[2])
print(figuraForca[3])
print(figuraForca[4])
print(figuraForca[5])
print(figuraForca[6])"""

# Criação do banco de palavras e apresentação
palavras = [ "Japao", "Alemanha", "Franca", "Espanha", "Romenia", "Argentina", "Brasil", "Nova-Zelandia",
            "Africa-do-Sul", "Costa-do-Marfim", "Egito", "Australia", "Arabia-Saudita", "Coreia-do-Sul", 
            "Honduras", "Mexico" ]

# print(random.choice(palavras))

#Criação da apresentação
print("=" * 80)
print(" " * 26, "Bem vindo ao JOGO DA FORCA")
print("=" * 80)

nome = input("Digite seu nome: ").title()
print(f"\n\nOlá {nome}, neste jogo você deverá advinhar a palavra sorteada!")
print()
print("-" * 80)
print()
print(" " * 12, "Dica: Países participantes das Olimpíadas Tokyo 2021\n")
print(" " * 12, "OBS.: Países com nome composto acrescente hífen '-' ")
print()
print("-" * 80)
print()

# Criação da função principal
def principal():
    """ Função principal
    Declarei as variaveis vazias e as condições de jogo, sendo:
    PARTIDA -> O jogo propriamente dito!
    CHUTE -> As tentativas "chutes!
    VITORIAJOGO -> A mensagem de vitória!"""
    

    letrasErradas = " " # Iniciamos esta variável
    letrasCertas = "" # Iniciamos esta variável
    palavraSorteada = palavraSorteadaEscolhida().upper() # Inicia a palavra sorteada
   
    partida = True
 
    while partida: # Enquanto o usuário estiver jogando (True)
        partidaJogo(letrasErradas, letrasCertas, palavraSorteada) # Em uma partida temos estas variáveis (erros, acertos e a palavra sorteada)
 
        chute = chutesJogo(letrasErradas + letrasCertas) # Garante que vou receber letras certas e erradas
 
        if chute in palavraSorteada: # Se o chute for certeiro
            letrasCertas += chute # Letras certas somam (1) + chute
 
            if vitoriaJogo(palavraSorteada, letrasCertas): # Verificamos se houve vitória
                print("===== Winner ===== | O país sorteado foi: ", palavraSorteada)
                partida = False
        else:
            letrasErradas += chute # Letras erradas somam (1) + chute
 
            if len(letrasErradas) == len(figuraForca) - 1: # Verifica-se o numero de letras erradas == Ao número de figuras da forca
                partidaJogo(letrasErradas, letrasCertas, palavraSorteada) # Imprime ERROS, ACERTOS e PAÍS SORTEADO
 
                print("===== Loser ===== | Você atingiu o limite de tentativas!")
                print("Depois de " + str(len(letrasErradas)) + " letras erradas e " + str(len(letrasCertas)) + " letras certas! ", end =" ")
                print("O país sorteado foi:  ",  palavraSorteada)
 
                partida = False
 
        if not partida: # Se o usuário estiver jogando (False)
            if jogarNovamente(): 
                letrasErradas = " "  # Reinicia esta variável
                letrasCertas = "" # Reinicia esta variável
                partida = True
                palavraSorteada = palavraSorteadaEscolhida().upper() # Reinicia a palavra sorteada
                
# Criação das funções de jogo
def palavraSorteadaEscolhida():
    
    """
    Funcao que inicia a palavra sorteada"""
    
    return random.choice(palavras)

def espacosJogo(palavra):
  
    """
    Função que retorna o espaço vazio entre as strings"""

    for letra in palavra:
        print(letra, end = " ")
 
    print()

def partidaJogo(letrasErradas, letrasCertas, palavraSorteada):

    """
    Função do jogo propriamente dito, possui as figuras, letras certas, letras erradas e o país sorteado"""

   
    print(figuraForca[len(letrasErradas)] + "\n")  # Imprime a qtde de letras erradas
 
    print("Letras Erradas: ", end = " ") # Letras erradas que receberão um espaço
    espacosJogo(letrasErradas) # Chama a função espacoJogo
 
    espaco = "_" * len(palavraSorteada) # Criação dos espaços que receberão/ serão substituidos pelas letras certas
    for i in range(len(palavraSorteada)): # Para cada letra certa, iremos varrer a palavra
        if palavraSorteada[i] in letrasCertas: # Se a palavra sorteada esta em letras
            espaco = espaco[:i] + palavraSorteada[i] + espaco[i+1:] # espaço recece = [espaço e todos que os antecedem] + [palavra sorteada] + [espaço atual + 1 + seus sucessores]
    espacosJogo(espaco) # A função espacoJogo imprime os espaços!

def chutesJogo(chutesON):

    '''Função que determina que o usuário digite apenas uma letra e
        confere se a mesma já não foi chutada'''
    
    while True: # Enquanto chutes forem verdadeiros
        chute = input("Digite uma letra: \n").upper()
        
        if len(chute) != 1: # Se o chute possui mais de uma letra
            print("Digite apenas uma letra!!!")
        elif chute in chutesON: # Caso os chutes sejam repetidos
            print('Letra repetida, tente novamente!!!')
        elif not "A" <= chute <= "Z" and chute == " ": # garante que o chute esteja dentro do alfabeto
            print("Cuidado!!! Você digitou um caracter inválido!!!")
        else:
            return chute  # Imprime o chute!!!!

# 5. Criação de solicitação de reinicio de jogo
def jogarNovamente():

    """
    Funcao que garante a opção de jogar ou não uma nova partida!"""
    
    return input("Voce quer jogar novamente? (S/N)\n").upper().startswith('S') # se a resposta do usuario convertido em maiusculo for verdadeiro

    """ Usar-> função startswith() é usada para verificar se uma determinada frase começa com alguma string particular.
        Os parâmetros de início e término são opcionais.
        
        Podemos usá-los quando quisermos que apenas alguma substring particular da string original seja considerada para pesquisa.
        
        Retorna -> o valor de retorno é binário. A função retorna True se a frase original começar com search_string, senão False .
        
        """

def vitoriaJogo(palavraSorteada, letrasCertas):
    
    '''
    Funcao que verifica se o usuario acertou todas as
    letras da palavra sorteada'''
    
    vitoria = True #nao precisaria
    for letra in palavraSorteada: # Percorre cada uma das letras da palavra sorteada
        if letra not in letrasCertas: # Se a letra não está dentros de letras certas
            vitoria = False # Se ela não estiver dentro das letras certas, retorna False
            break 
            # return False
    return vitoria #True
    
principal()
