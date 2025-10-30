"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude leia,
lendo o nome deles e escrevendo o nome do escolhido."""

import random
from time import sleep

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
sorteio = [aluno1, aluno2, aluno3, aluno4]
print('SUSPENSE ... tchananannnn  tchananannnn')
sleep(5)
print(f'O aluno sorteado foi para apagar o quadro foi {random.choice(sorteio)}')
