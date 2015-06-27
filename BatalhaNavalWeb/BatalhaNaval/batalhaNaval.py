class Jogo:
	LARGURA = 64
	ALTURA = 64

	def __init__(self):
		self.tabuleiro = map(lambda i: map(lambda x: False, range(Jogo.ALTURA)), range(Jogo.LARGURA))

	def colocarBarcoEm(self, x, y):
		self.tabuleiro[x][y] = True

	def atirarEm(self, x, y):
		self.tabuleiro[x][y] = False

	def posicaoPossuiBarco(self, x, y):
		return self.tabuleiro[x][y]

	@property
	def estaAcabado(self):
		for linha in self.tabuleiro:
			if any(linha):
				return False

		return True