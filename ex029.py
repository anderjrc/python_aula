"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 cada km acima do limite."""

velocidade = int(input('Qual é a velocidade atual do carro? '))
#permitido = 80
if velocidade <= 80:
    print('PARABÉNS! Tenha um bom dia! Diriga com segurança')
else:
    print(f"MULTADO! Você excedeu o limite permitido que é de 80km/h\n"
          f"Você deve pagar uma multa de R$ {(velocidade - 80) * 7:.2f}\n"
          f"Tenha um bom dia! Diriga com segurança!")
