from random import randint
from time import sleep
import emoji

itens = ['pedra 👊', 'papel 🫲', 'tesoura 🖖']
computador = randint(0, 2)
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 14)
print(emoji.emojize(f'O computador jogou {itens[computador]}'))
print(emoji.emojize(f'O jogador jogou {itens[jogador]}'))
print('-=' * 14)
if computador == 0:
    if jogador == 0:
        print('\033[33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[34mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[34mJOGADOR VENCEU\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('\033[34mJOGADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[33mEMPATE\033[m')
    else:
        print('JOGADA INVÁLIDA!')
