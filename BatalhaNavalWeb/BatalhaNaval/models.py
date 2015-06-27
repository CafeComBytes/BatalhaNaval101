from django.db import models
from batalhaNaval import Jogo

jogo = Jogo()

jogo.colocarBarcoEm(2, 2)

def obter_jogo():
	global jogo
	
	return jogo