"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar
ou se já passou do tempo de alistamento. Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo."""

"""ano = int(input("Ano do nascimento: "))
idade = 2025 - ano
maioridade = 18  #idade para se alistar
print(f"Quem nasceu em {ano} tem {idade} anos em 2025.")
if ano > 2007:
    print(f"Ainda falta {maioridade - idade} anos para o alistamento.\n"
          f"Seu alistamento será em {idade + 2025}.")
elif ano == 2007:
    print(f"Está na hora do seu alistamento. Diriga-se a Junta Militar mais próxima!")
else:
    print(f"Já passaram {idade - maioridade} anos do prazo do seu alistamento.\n"
          f"Seu alistamento foi {2025 - (idade - maioridade)}")"""

#podemos fazer assim também
from datetime import date
ano_atual = date.today().year
ano_nasc = int(input("Ano do nascimento: "))
idade = ano_atual - ano_nasc
print(f"Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}")
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE")
elif idade < 18:
    print(f"Ainda falta {18 - idade} anos para o alistamento.")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")