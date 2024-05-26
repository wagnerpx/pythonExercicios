from random import randint
from time import sleep
computador = randint(0, 10)
print('\033[33m-=-\033[m' * 20)
print('Vou pensar em um número entre "0" e "10". Tente adivinhar...')
print('\033[33m-=-\033[m' * 20)
jogador = int(input('Em que número eu estou pensando? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você ganhou.')
else:
    print('ERROU! Eu pensei no número "{}" e não no "{}"'.format(computador, jogador))
