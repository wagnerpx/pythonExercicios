núm = int(input('Digite um número: '))
total = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, total))
if total == 2:
    print('por isso ele é \033[33mPRIMO\033[m')
else:
    print('por isso ele NÃO É PRIMO')
