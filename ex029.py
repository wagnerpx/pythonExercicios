
from time import sleep
velocidade = float(input('Qual a velocidade do carro: '))
if velocidade > 80:
    print('\033[7;31;40mMULTADO!\033[m você excedeu o limite permitido que é 80Km/h.')
    multa = (velocidade - 80) * 7
    print('Gerando a sua Multa...')
    sleep(3)
    print(f'O valor da multa é R$ {multa}')
print('\033[33mTenha um bom dia! Dirija com segurança!')
