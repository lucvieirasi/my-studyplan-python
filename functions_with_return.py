"""
Funções com retorno


"""
"""
numeros = [1, 2, 3]

rest_pop = numeros.pop()
print(f'Retorno de pop: {rest_pop}')

rest_pr = print(numeros)

print(f'Retorno de print: {rest_pr}')

# Vamos refatorar está função para que ela retorne o valor
# OBS: Funções Python que retornam valores, devem retornas os valores com a palavra return.
# Não precisamos necessariamente criar uma variável para receber o retorno de uma função, podemos passar a execução de uma função,
# Para outras funções até mesmo print.

def quadrado_de_7():
	return 7 * 7


# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7() + 1}')
"""
# Refatorando a primeira função:

"""
def diz_oi():
	return 'Oi '

alguem = 'pedro!'
print(diz_oi() + alguem)
"""

"""
OBS: 
1 - Ela finaliza a função, ou seja, ela sai da execução da função.
2 - Podemos ter, em uma função, diferentes returns.
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores.
"""

"""
# Exemplo 1

def diz_oi():
	print('Estou sendo executado antes do retorno...')
	return 'Oi'


print('Estou sendo executado após do retorno...')

print(diz_oi())
"""

"""
# Exemplo 2

def nova_funcao():
	variavel = False
	if variavel:
		return 4
	elif variavel is None:
		return 3.2
	return 'B'


print(nova_funcao())


# Exemplo 3

def outra_funcao():
	return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_funcao()
#
# print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))
"""


# Exemplo 3

# Vamos criar uma função para jogar a moeda (cara ou coroa)

# from random import random
#
#
# def joga_moeda():
# 	# Gera um numero psudo-randomico entre 0 e 1
# 	if random() > 0.5:
# 		return 'Cara'
# 	return 'Coroa'
#
#
# print(joga_moeda())

def eh_impar():
	numero = 6
	if numero % 2 != 0:
		return True
	return False


print(eh_impar())
