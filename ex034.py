salário = float(input('Qual é o salário do funcionário? R$'))

if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava \033[031mR${:.2f}\033[m passa a ganhar \033[34mR${:.2f}\033[m agora.'.format(salário, novo))
