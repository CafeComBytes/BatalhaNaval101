import unittest
from batalhaNaval import Jogo

class BatalhaNavalTeste(unittest.TestCase):

	def setUp(self):
		self.jogo = Jogo()
		self.jogo.colocarBarcoEm(5, 5)


	def testa_que_acertou_um_barco(self):
		self.assertTrue(self.jogo.posicaoPossuiBarco(5, 5))

		self.jogo.atirarEm(5, 5)

		self.assertFalse(self.jogo.posicaoPossuiBarco(5, 5))
		

	def testa_houve_vitoria(self):
		self.jogo.atirarEm(5, 5)

		acabouOjogo = self.jogo.estaAcabado

		self.assertTrue(acabouOjogo)

	def testa_que_nao_acertou_um_missel(self):
		assert not self.jogo.posicaoPossuiBarco(1, 1)
		
		self.jogo.atirarEm(1, 1)

		assert not self.jogo.posicaoPossuiBarco(1, 1)


unittest.main()