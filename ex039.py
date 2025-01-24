from datetime import date
atual = date.today().year
print('''Escolha uma das Opções abaixo
Masculino [1]
Feminino  [2]''')
opção = int(input('Sua opção: '))
lista = [1, 2]
for n in lista:
    if opção == 1:
        print('Seja bem vindo!')
        break
    else:
        print('Inscrições Feminina pelo site.')
        break
nasc = int(input('Ano de nascimento: '))
idade = (atual - nasc)
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Este é o ano do seu ALISTAMENTO!')
elif idade < 18:
    saldo = 18 - idade
    print('falta {} ano(s), va aproveitar a JUVENTUDE!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Espero sinceramente que vc já tenha se alistado ou estára atrasado em {} ano(s)!'.format(saldo))
    ano = atual - saldo
    print('O ano do seu alistamento foi {}'.format(ano))

