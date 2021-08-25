'''
003 - Sorveteria.py
Vendas: Picolés
Preço: Unitário


ABSTRAÇÃO -> O que a sorveteria precisa ter! Exatamente a qtde de coisas que preciso!
    preciso = [vender e cobrar] -> receberPedido

'''


class Sorveteria(object):
    def __init__(self, estoque, precoUnitario, caixa): # abstração | atributos
        self.estoque = estoque
        self.precoUnitario = precoUnitario
        self.caixa = caixa

    def receberPedido(self, numSorvetes): #qtde de coisas que o cliente quer para fazer um pedido
        ''' 
        Envolvimento de estoques e precoUnitario
        
        '''
        try: 
            if numSorvetes > 0:
                raise ValueError('Qtde invalida')

            if numSorvetes > self.estoque:
                raise SystemError('Estoque indisponivel')

            self.estoque -= numSorvetes    
            print(f'Sorveteria - Pedido de {numSorvetes} sorvetes efetuados. Estoque - {self.estoque}. Valor do pedido -: R$ {numSorvetes * self.estoque}')
            '''PRINT -> Nome da classe - Informações relevantes'''

            return numSorvetes * self.precoUnitario

        except ValueError:
            print(f'Sorveteria - Pedido de {numSorvetes} sorvetes não efetuados por qtde invalida. Estoque: {self.estoque}')
            return 0 # nao me deve nada

        except SystemError:
            print(f'Sorveteria - Pedido de {numSorvetes} sorvetes não efetuados por falta de estoque. Estoque: {self.estoque}')
            return 0 # nao me deve nada

        except:
            print(f'Sorveteria - Pedido de {numSorvetes} sorvetes não efetuados . Estoque: {self.estoque}')
            return 0 # nao me deve nada 

    def receberPagamento(self, valorConta, valorPagamento):
        '''
        Cenários Fictícios (felizes):
        1. O cliente da o valor correto
        2. O cliente da uma valor com troco
        3. O cliente quer pagar parcial
        '''
        try: 
            if valorConta <= 0 or valorPagamento <=0: # conta negativa ou pgto negativo
                raise ValueError('Valor(es) invalido(s)')

            if valorConta == valorPagamento:
                self.caixa += valorPagamento
                print(f'Sorveteria - Conta paga totalmente, recebido R${valorPagamento}, conta R${valorConta}. Caixa: {self.caixa}')
                return 0

            elif valorConta < valorPagamento:
                self.caixa += valorConta
                print(f'Sorveteria - Conta paga totalmente com troco de R$ {valorPagamento - valorConta}, recebido R${valorPagamento}, conta R${valorConta}. Caixa: {self.caixa}')
                return -(valorPagamento - valorConta) # Devolvo uma comanda negativa para o estabelecimento, ou seja, comanda positiva para o cliente == devolvendo o troco

            else:
                self.caixa += valorPagamento
                print(f'Sorveteria - Conta paga parcialmente, restam  R${valorConta - valorPagamento}, recebido R${valorPagamento}, conta R${valorConta}. Caixa: {self.caixa}')
                return valorConta - valorPagamento
        
        except ValueError:
            print(f'Sorveteria - Erro ao pagar conta, valor (es) invalidos(s), recebido  R${valorPagamento}, recebido R${valorPagamento}, conta R${valorConta}. Caixa: {self.caixa}')
            return valorConta

        except:
             print(f'Sorveteria - Erro ao pagar conta, recebido  R${valorPagamento}, recebido R${valorPagamento}, conta R${valorConta}. Caixa: {self.caixa}')
             return valorConta


class Cliente(object):
    def __init__(self, nome, carteira, conta):
        self.nome = nome
        self.carteira = carteira
        self.conta = 0.0

    def fazPedido(self, numSorvetes, objsorveteria): # sorveteria é um objeto que uso como atributo proveniente da classe Sorveteria
        try:
            if numSorvetes <= 0:
                raise ValueError('Qtde invalida')
            if not isinstance(objsorveteteria, Sorveteria):
                raise SystemError('Não recebeu uma sorveteria')

            self.conta += sorveteria.receberPedido(numSorvetes) # puxo receberPedido de outra classe
            print(f'Cliente {self.nome} - Pedido de {numSorvetes} sorvetes feitos. Conta: R$ {self.conta}')
            return self.conta #conta é alterada conforme o pedido vai acontecendo
        
        except ValueError:
            print(f'Cliente {self.nome} - Pedido de {numSorvetes} sorvetes não efetuado, por qtde invalida. Conta: R$ {self.conta}')
            return -1
        
        except SystemError:
            print(f'Cliente {self.nome} - Pedido de {numSorvetes} sorvetes não efetuado, por sorveteria invalida. Conta: R$ {self.conta}')
            return -1 # testar se meus erros sao tratados pelos TRY nos testes unitarios
           
        except:
            print(f'Cliente {self.nome} - Pedido de {numSorvetes} sorvetes não efetuado. Conta: R$ {self.conta}')
            return self.conta #conta é alterada conforme o pedido vai acontecendo


    def pagaConta(self, valorPgto, objsorveteria):
        try:
            if valorPgto <= 0:
                raise ValueError('Valor invalido')

            if valorPgto > self.carteira:
                raise ArithmeticError('Pgto maior que dinheiro disponivel')

            if not isinstance(objsorveteria, Sorveteria): #objSorveteria nao for uma instancia de Sorveteria
                raise SystemError('Não recebeu sorveteria')

            self.carteira = carteira
            divida = objsorveteria.receberPagamento(self.conta, valorPgto)
            if divida ==  0:
                self.conta = divida

            elif divida > 0: 
                self.conta= divida
            else:
                self.carteira -= divida
                self.conta = 0
            print(f'Cliente - {self.nome} - Pagamento de R$ {valorPgto} da conta de R$ {self.conta}. Carteira: R$ {self.carteira} ')
            return self.carteira # só para os testes
        

        except ValueError:
            print(f'Cliente - {self.nome} - Pagamento de R$ {valorPgto} da conta de R$ {self.conta} nao foi efetuado pois o valor do pgto nao é valido. Carteira: R$ {self.carteira} ')
            return -1

        except ArithmeticError:
            print(f'Cliente - {self.nome} - Pagamento de R$ {valorPgto} da conta de R$ {self.conta} nao foi efetuado pois o valor do pgto é superior. Carteira: R$ {self.carteira} ')
            return -1

        except SystemError:
            print(f'Cliente - {self.nome} - Pagamento de R$ {valorPgto} da conta de R$ {self.conta} nao foi efetuado pois sorveteria nao é validoor. Carteira: R$ {self.carteira} ')
            return -1

        except:
            print(f'Cliente - {self.nome} - Pagamento de R$ {valorPgto} da conta de R$ {self.conta} nao foi efetuado. Carteira: R$ {self.carteira} ')
            return -1
s = Sorveteria(10, 1.5, 0)