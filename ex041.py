"""A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL         Até 25 anos: SÊNIOR
- Até 19 anos: JUNIOR           Acima: MASTER"""

from datetime import date
ano_atual = date.today().year
ano_nasc = int(input("Ando de nascimento: "))
idade = ano_atual - ano_nasc
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classifiação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")