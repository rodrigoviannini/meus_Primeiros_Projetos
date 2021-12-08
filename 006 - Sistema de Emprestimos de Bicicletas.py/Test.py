import unittest
import datetime
from Codigo import Loja, Cliente

class Testes(unittest.TestCase):
    def setUp(self):
        self.cliente = Cliente(0, 0, 0)
        self.loja = Loja(40)

    # ESTOQUE
    def testeMostrarEstoque(self):
        print("\nTeste - Mostrar Estoque\n")
        self.assertEqual(self.loja.mostrarEstoque(), 40)

    # HORA
    # Corrigir o Teste Locacao Hora Valida
    '''def testeLocacaoHoraValido(self):
        print("\nTeste - Locação Hora VALIDO")
        self.assertEqual(self.loja.locacaoHora(3, True), None)'''

    def testeLocacaoHoraNumInvalido(self):
        print("\nTeste - Locação Hora Numero Inválido")
        self.assertEqual(self.loja.locacaoHora(-1, True), False)

    def testeLocacaoHoraZeroBike(self):
        print("\nTeste - Locação Hora Zero Bike")
        self.assertEqual(self.loja.locacaoHora(0, True), False)

    def testeLocacaoHoraMaior(self):
        print("\nTeste - Locação Hora Maior")
        self.assertEqual(self.loja.locacaoHora(41, True), False)

    # DIA
    def testeLocacaoDiaNumInvalido(self):
        print("\nTeste - Locação Dia Numero Inválido")
        self.assertEqual(self.loja.locacaoDia(-1, True), False)
    
    def testeLocacaoDiaZeroBike(self):
        print("\nTeste - Locação Dia Zero Bike")
        self.assertEqual(self.loja.locacaoDia(0, True), False)

    def testeLocacaoDiaMaior(self):
        print("\nTeste - Locação Dia Maior")
        self.assertEqual(self.loja.locacaoDia(41, True), False)
    
    # SEMANA 
    def testeLocacaoSemanaNumInvalido(self):
        print("\nTeste - Locação Semana Numero Inválido")
        self.assertEqual(self.loja.locacaoSemana(-1, True), False)

    def testeLocacaoSemanaZeroBike(self):
        print("\nTeste - Locação Semana Zero Bike")
        self.assertEqual(self.loja.locacaoSemana(0, True), False)

    def testeLocacaoSemanaMaior(self):
        print("\nTeste - Locação Semana Maior")
        self.assertEqual(self.loja.locacaoSemana(41, True), False)

    # FAMILIA
    def testeLocacaoFamiliaBikes(self):
        print("Teste -Locação Familia Tres Bikes")
        self.assertEqual(self.loja.locacaoFamilia(3==4==5, True), False)

   
if __name__ == "__main__":
    unittest.main()