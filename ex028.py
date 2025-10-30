"""Escreva um progrma que faça o computador 'pensar em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
usuário venceu ou perdeu."""

from random import randint
from time import sleep

print('--=' * 20)
print('Vou pensar um em número entre 0 e 5. Tente adivinhar ...')
print('-=-' * 20)
computador = randint(0,5) #faz o computador pensar em um número aleatório
jogador = int(input('Em que número pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO ...')
sleep(2) #tempo para pensar

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer :)')
elif jogador > 5:
    print('Este número não é válido!')
else:
    print(f"Você perdeu! Eu pensei no número {computador}.")

