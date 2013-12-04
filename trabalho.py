import os
TAMANHO_MAXIMO = 11
nomeArquivo = "trabalho"

class Pessoa:
	def __init__(self,chave,nome,idade):
		self.chave 	= chave
		self.nome 	= nome
		self.idade	= idade
	
	def getChave(self):
		return self.chave
	def getNome(self):
		return self.nome
	def getIdade(self):
		return self.idade

def main():
	pessoa = Pessoa(20,"Euler Satnana",23)
	print "Chave:",pessoa.getChave()

if __name__== '__main__':
	main()