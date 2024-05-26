número = int(input('Digite um número: '))
resultado = número % 2

if resultado == 1:
    print(f'O número {número} é \033[34mÍMPAR\033[m')
else:
    print(f'O número {número} é \033[34mPAR\033[m')
