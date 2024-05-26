from datetime import date
ano = int(input('Qual ano quer analisar? Coloque 0 para o ano atual! '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[34m{}\033[m é \033[36mBISSEXTO\033[m'.format(ano))
else:
    print('O ano \033[31m{}\033[m não é \033[36mBISSEXTO\033[m'.format(ano))
