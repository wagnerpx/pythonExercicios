n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(f'Sua media foi {media} \033[34m"APROVADO"\033[m')
elif 7 > media >= 5:
    print(f'Sua media foi {media} \033[33m"Recuperação"\033[m')
else:
    print(f'Sua media foi {media} \033[31m"REPROVADO"\033[m')
