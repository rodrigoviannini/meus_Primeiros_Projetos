"""
    Let's Code | Projeto 3
    Sistema de Empréstimo de Bicicletas

    Alunos: Rodrigo Viannini
            Leonardo Azevedo

"""
# Necessidades e Expectativas

"""
        Sistema de Empréstimo de Bicicletas

        Vocês farão em duplas ou trios um sistema de empréstimo de bibliotecas, que envolverá duas classes principais (Cliente, Loja) e uma para testes unitários (TestaEmprestimoBikes). O projeto deve ser apresentado na última aula do módulo (30/08/2020).

        Cliente pode:
        Ver as bicicletas disponíveis na Loja;
        Alugar bicicletas por hora (R$5/hora);
        Alugar bicicletas por dia (R$25/dia);
        Alugar bicicletas por semana (R$100/semana)
        Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos (de qualquer tipo) com 30% de desconto no valor total.

        Loja pode:
        Calcular a conta quando o cliente decidir devolver a bicicleta;
        Mostrar o estoque de bicicletas;
        Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
        Por questão de simplicidade vamos assumir que:
        Cada empréstimo segue apenas um modelo de cobrança (hora, dia ou semana);
        O cliente pode decidir livremente quantas bicicletas quer alugar;
        Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes disponíveis.
"""
import datetime

#import pytz

"""
    import pytz

    você já está usando a biblioteca pytz, que pode analisar (de acordo com algumas regras de desambiguação arbitrárias, mas bem definidas) formatos como “EST”. Então, se você realmente quiser, você pode deixar o %Z no lado de formatação, então retire-o e analise-o com pytz.timezone() antes de passar o resto para strptime.
"""

#from math import *


class Cliente(object):
    def __init__(self, qtdeBikes, opcaoLocacao, tempoLocacao):
        self.qtdeBikes = qtdeBikes
        self.opcaoLocacao = opcaoLocacao
        self.tempoLocacao = tempoLocacao
        

    def mostrarEstoque(self, estoque): # estoque == Loja
        """ Imprimir quantidade disponível de bicicletas no estoque """
        return estoque.mostraEstoque()
        

    def AlugarBikes(self, qtdeBikes, opcaoLocacao, estoque):
        self.qtdeBikes = qtdeBikes
        self.opcaoLocacao = opcaoLocacao
        self.estoque.estoque

        # qtdeBikes = int(input("Quantas unidade deseja locar: "))

        if opcaoLocacao == 1: # Criar _> def locacaoHora
            self.prazoLocacao = estoque.locacaoHora(self.qtdeBikes, estoque)
        elif opcaoLocacao == 2:
            self.prazoLocacao = estoque.locacaoDia(self.qtdeBikes, estoque)
        elif opcaoLocacao == 3:
            self.prazoLocacao = estoque.locacaoSemana(self.qtdeBikes, estoque)
        self.opcaoLocacao = opcaoLocacao
        return self.qtdeBikes, self.opcaoLocacao, self.tempoLocacao # Parâmetros da -> def __init__

class Loja(object):
    def __init__(self, estoqueLoja):
        self.estoqueLoja = estoqueLoja
        # Essa classe não preciso retornanr nada
        self.bikes = 40

    def mostrarEstoque(self):
        """ Imprimir quantidade disponível de bicicletas no estoque """
        print("Estoque: ", self.estoqueLoja)
        return self.estoqueLoja 
        # Uso o self para puxar da classe Loja

    def locacaoHora(self, qtdeBikes, cliente):
        self.cliente = cliente
        """
            Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes disponíveis.

            ALUGUEL + VALIDAÇÃO
        """
        if qtdeBikes <= 0:
            # Evitar que o usuário digite um numero negativo
            print("Quantidade inválida!")
            return False

        elif qtdeBikes > self.estoqueLoja:
            # Evitar que a qtde de bikes solicitadas seja maior que o estoque
            print("Quantidade indisponível de bicicletas")
            return False

        else:
            # Estoque disponível -> retorno a hora atual (cálculo do tenpo de locação)
            tempoLocacao = datetime.datetime.now()
            print(f"Qtde: {qtdeBikes} | Hora: {tempoLocacao.strftime('%d.%m.%Y %H:%M:%S - %d.%m.%Y %H:%M:%S')}")
            # Fonte -> Hora <https://www.programiz.com/python-programming/datetime/strftime>
            
            self.estoqueLoja -= qtdeBikes
            return tempoLocacao

    def locacaoDia(self, qtdeBikes, cliente):

        self.cliente = cliente # -> Não é necessário, pq já contem na classe acima

        """
            Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes disponíveis.

            ALUGUEL + VALIDAÇÃO
        """
        if qtdeBikes <= 0:
            # Evitar que o usuário digite um numero negativo
            print("Quantidade inválida!")
            return False

        elif qtdeBikes > self.estoqueLoja:
            # Evitar que a qtde de bikes solicitadas seja maior que o estoque
            print("Quantidade indisponível de bicicletas")
            return False

        else:
            # Estoque disponível -> retorno a hora atual (cálculo do tenpo de locação)
            tempoLocacao = datetime.datetime.now()
            print(f"Qtde: {qtdeBikes} , Hora: {tempoLocacao.strftime('%d.%m.%Y %H:%M:%S - %d.%m.%Y %H:%M:%S')}")
            # Fonte -> Hora <https://www.programiz.com/python-programming/datetime/strftime>
            
            self.estoqueLoja -= qtdeBikes
            return tempoLocacao        


    def locacaoSemana(self, qtdeBikes, cliente):
        
        # self.cliente = cliente -> Não é necessário, pq já contem na classe acima

        """
            Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes disponíveis.

            ALUGUEL + VALIDAÇÃO
        """
        if qtdeBikes <= 0:
            # Evitar que o usuário digite um numero negativo
            print("Quantidade inválida!")
            return False

        elif qtdeBikes > self.estoqueLoja:
            # Evitar que a qtde de bikes solicitadas seja maior que o estoque
            print("Quantidade indisponível de bicicletas")
            return False

        else:
            # Estoque disponível -> retorno a hora atual (cálculo do tenpo de locação)
            tempoLocacao = datetime.datetime.now()
            print(f"Qtde: {qtdeBikes} | Hora: {tempoLocacao.strftime('%d.%m.%Y %H:%M:%S - %d.%m.%Y %H:%M:%S')}")
            # Fonte -> Hora <https://www.programiz.com/python-programming/datetime/strftime>
            
            self.estoqueLoja -= qtdeBikes
            return tempoLocacao


    def locacaoFamilia(self, qtdeBikes, cliente):
        """ 
            Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos (de       qualquer tipo) com 30% de desconto no valor total.
        """
        
        if qtdeBikes >= 3 and qtdeBikes <= 5:
            print(f"Qtde: {qtdeBikes}, tem direito ao desconto de 30%")
            return True
        else:
            print("Desconto válido para a qtde entre 3 a 5 bicicletas")
            return False

    #def custoLocacao(self, clienteLocacao, locacaoFamilia):
        """ Calcular a conta quando o cliente decidir devolver a bicicleta """

    # Verificar os testes e fazer a função de calculo!