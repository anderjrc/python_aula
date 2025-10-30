"""Crie um programa que leia o nome de uam cidade e diga se ela começa ou não com o nome SANTO"""

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')

'''import re

pergunta = str(input('Em que cidade você nasceu? '))
cidade = 'santo'

if re.search(cidade, pergunta, re.IGNORECASE):
    print(f'A palavra {cidade} foi encontrada.')
else:
    print('A palavra não foi encontrada.')'''



