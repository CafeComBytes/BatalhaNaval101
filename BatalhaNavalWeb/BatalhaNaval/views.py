from django.shortcuts import render, redirect
from BatalhaNaval.models import obter_jogo

def exibir_tabuleiro(requisicao):
	return render(requisicao, "exibir_tabuleiro.html", {"jogo": obter_jogo()})

def atacar(requisicao):
	posicaoX = int(requisicao.POST["posicaoX"])
	posicaoY = int(requisicao.POST["posicaoY"])
	obter_jogo().atirarEm(posicaoX, posicaoY)
	return redirect("/tabuleiro")

