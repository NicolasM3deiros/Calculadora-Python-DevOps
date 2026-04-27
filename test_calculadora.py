import unittest
from Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        # Inicia a calculadora e a interface antes de cada teste
        self.app = Calculadora()
        self.app.update()

    def tearDown(self):
        # Fecha a calculadora após cada teste
        self.app.destroy()

    def test_soma(self):
        self.app.display.insert(0, '2+2')
        self.app.clique('=')
        self.assertEqual(self.app.display.get(), '4')

    def test_subtracao(self):
        self.app.display.insert(0, '10-5')
        self.app.clique('=')
        self.assertEqual(self.app.display.get(), '5')

    def test_multiplicacao(self):
        self.app.display.insert(0, '3*4')
        self.app.clique('=')
        self.assertEqual(self.app.display.get(), '12')

    def test_divisao_por_zero(self):
        self.app.display.insert(0, '10/0')
        self.app.clique('=')
        self.assertEqual(self.app.display.get(), 'Erro')

    def test_limpar_visor(self):
        self.app.display.insert(0, '123')
        self.app.clique('C')
        self.assertEqual(self.app.display.get(), '')

if __name__ == '__main__':
    unittest.main()