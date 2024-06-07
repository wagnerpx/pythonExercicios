from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = (atual - nasc)
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Vc tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('falta {} ano(s), va aproveitar a JUVENTUDE!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Vc já deveria ter se alistado! está atrasado {} ano(s)!'.format(saldo))
    ano = atual - saldo
    print('O ano do seu alistamento foi {}'.format(ano))

