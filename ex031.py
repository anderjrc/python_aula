"""Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200km e 0,45 para viagens mais longas."""

distancia = int(input('Qual é a distância da sua viagem: '))
if distancia <= 200:
    print(f"O valor da passagem ficara R$ {distancia * 0.50:.2f}")# preço == 0.50 por km
else:
    print(f"O valor da passagem ficara R$ {distancia * 0.45:.2f}")# preço == 0.45 por km

