import unittest
from Main import Sorveteria, Cliente

class Testes(unittest.TestCase):
    def setUp(self):
        self.s = Sorveteria(10, 1.5, 0)
        self.c = Cliente("Pedro", 10)


    def testeRecebePedido(self):
        print('\nTeste de sorveteria receber pedido') #log
        self.assertEqual(self.s.receberPedido(2), 3) # no lugar de 3 coloco 4 para ver o ERRO

    def testeRecebePedidoSemEstoque(self):
        print('\nTeste de sorveteria receber pedido acima do estoque') #log
        self.assertEqual(self.s.receberPedido(11), 0)

    def testeRecebePedidoInvalido(self):
        print('\nTeste de sorveteria receber pedido invalido') #log
        self.assertEqual(self.s.receberPedido(-3), 0)

if __name__ == '__main__':
    unittest.main()