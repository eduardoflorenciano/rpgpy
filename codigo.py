# Importa biblioteca para ler o arquivo CSV que contém os dados da planilha
import csv

# Importa biblioteca para gerar números aleatórios, o que influenciará nas probabilidades de escolha do usuário
import random

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Função que abre e lê o arquivo txt
with open("apresentacao.txt") as minhaApresentacao:
	minhaVariavel = minhaApresentacao.read()

# Imprime o arquivo txt
print(minhaVariavel)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Declara vetor vazio
planilha = []

# Função que imprime apenas 'Aventuras' da planilha
def imprimirAventuras(planilha):

	# Imprime cada linha do csv dicionarizado
	for eduardo in planilha:
		print(f"Aventura: {eduardo['Aventura']}")

# Função que imprime apenas uma 'Aventura' específica
def aventuraEspecifica(planilha, elementoEspecifico):

	# Imprime cada linha do csv dicionarizado
	for eduardo in planilha:
		if eduardo == elementoEspecifico:
			print(f"Aventura: {eduardo['Aventura']}")

# Função que remove apenas uma 'Aventura' específica
def removerAventura(planilha, elementoRemovido):

	# Imprime cada linha do csv dicionarizado
	for eduardo in planilha:
		if eduardo != elementoRemovido:
			print(f"Aventura: {eduardo['Aventura']}")

# Função que solicita ao usuário digitar 'continue' para avançar
def funcaoContinue():
    escolha = input("Digite 'continue' para avançar: ")

    # Se o usuário não digitar certo, aparecerá uma mensagem negativa
    while escolha != "continue":
        escolha = input("Não foi possível avançar. Digite 'continue': ")
    
    # Se o usuário digitar corretamente, aparecerá uma mensagem positiva
    if escolha == "continue":
         print("Pode avançar, boa sorte!")
    
    # Retorna todas as modificações para a variável 'escolha'
    return escolha

# Função que abre e lê o arquivo csv
with open("rpg.csv", "r") as minhaPlanilha:
	novaVariavel = csv.DictReader(minhaPlanilha)

	# Coloca cada linha do csv em um elemento do vetor
	for n in novaVariavel:
		planilha.append(n)

# Imprime a planilha dicionarizada em formato de um vetor de objetos
print(planilha)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Função 1 declarada
imprimirAventuras(planilha)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Índice do vetor específico declarado
elementoEspecifico = planilha[9]

# Função 2 declarada
aventuraEspecifica(planilha, elementoEspecifico)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Índice do vetor específico declarado
elementoRemovido = planilha[19]

# Função 3 declarada
removerAventura(planilha, elementoRemovido)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Função 4 declarada
funcaoContinue()

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Função que abre e lê o arquivo txt
def lerIntroducao(apresentacaoTxt):
	with open(apresentacaoTxt) as arquivoIntroducao:
		variavelQualquer = arquivoIntroducao.read()
	
    # Retorna o arquivo para a 'variávelQualquer'
	return variavelQualquer

# Função que lê a planilha
def lerPlanilha(rpgCsv):
	# Declara vetor vazio
    planilha = []
	
    # Irá iterar (ler) cada linha da planilha
    with open(rpgCsv, 'r') as arquivoPlanilha:
        lerCsv = csv.DictReader(arquivoPlanilha)
        for linha in lerCsv:
            planilha.append(linha)

	# Todas as linhas ficarão armazenadas no vetor vazio
    return planilha

# Função que imprime as aventuras
def mostrarAventura(aventura):
	# Print para separar da introdução
	print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
	# Immprime qual é o cenário da história
	print(f"Cenário: {aventura['Cenario']}")
	
	# Imprime o número da aventura
	print(f"Situação {aventura['Situacao']}: {aventura['Aventura']}")
	
	# Imprime a alternativa A
	print(f"A) {aventura['Escolha A)']}")
	
	# Imprime a alternativa B
	print(f"B) {aventura['Escolha B)']}")

# Função que calcula a probabilidade as alternativas
def processarEscolha(aventura, escolha):
	
	# Se a escolha for A (maiúsculo) ou a (minúsculo)
	if escolha == 'A' or escolha == 'a':
		
		# Está como inteiro porque na planilha está como string, e precisa estar como inteiro para fazer a comparação com o número aleatório fornecido pelo random
		porcentagem = int(aventura['Porcentagem A)'])
		
		# Está com o valor da probabilidade de sucesso
		probabilidadeSucesso = aventura['Probabilidade de sucesso A)']
		
		# Está com o valor da probabilidade de fracasso
		probabilidadeFracasso = aventura['Probabilidade de fracasso A)']
		
    # Se a escolha for B (maiúsculo) ou b (minúsculo)
	elif escolha == 'B' or escolha == 'b':
		# Está como inteiro porque na planilha está como string, e precisa estar como inteiro para fazer a comparação com o número aleatório fornecido pelo random
		porcentagem = int(aventura['Porcentagem B)'])
		
		# Está com o valor da probabilidade de sucesso
		probabilidadeSucesso = aventura['Probabilidade de sucesso B)']
		
		# Está com o valor da probabilidade de fracasso
		probabilidadeFracasso = aventura['Probabilidade de fracasso B)']
		
    # Se não escrever nenhuma das opções, será retornado como invalido
	else:
		return "invalido", "Não escolheu nenhuma das opções."
	
    # Gera um número aleatório para determinar sucesso ou fracasso
	if random.randint(1, 100) <= porcentagem:
		return "sucesso", probabilidadeSucesso
	else:
		return "fracasso", probabilidadeFracasso

# Variáveis das funções

# Introdução
introducao = lerIntroducao("apresentacao.txt")
print(introducao)

# Leitura da planilha
planilha = lerPlanilha("rpg.csv")

# For loop de aventuras
for aventura in planilha:
	
	# Função
	mostrarAventura(aventura)
	
	# Para o usuário escolher as alternativas
	escolha = input("Escolha A ou B: ")
	
    # Função e print dos resultados das probabilidades (consequências) das alternativas
	probabilidade, resultado = processarEscolha(aventura, escolha)
	print(resultado)
	
    # Se a probabilidade for um fracasso, o jogo termina imediatamente
	if probabilidade == "fracasso":
		print("Você perdeu. Fim de jogo!")
		break
	
    # Se a probabilidade for um sucesso, o jogo seguirá adiante
	elif probabilidade == "sucesso":
		print("Parabéns! Você conseguiu avançar para a próxima aventura!")
		
    # Se não escolher nenhuma das opções ou digitar errado, o jogo termina imediatamente
	else:
		print("Perdeu todo o progresso do jogo!")
		break

# Se terminar o jogo, o usuário vence
else:
	print("Você venceu! Conseguiu voltar para casa em segurança!")