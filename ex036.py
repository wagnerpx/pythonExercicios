valor = float(input('Qual o valor da casa? '))
salário = float(input('Qual é o seu salário? '))
tempo = int(input('Em quantos anos você quer pagar? '))
print('=' * 30)
print('Valor da casa R${:.2f}'.format(valor))
print('Salário R${:.2f}'.format(salário))
print('Período {} anos'.format(tempo))
print('*' * 30)
tempo = tempo * 12
prestação = valor / tempo
limite = (salário * 30 / 100)
print('Tempo {:.0f} parcelas'.format(tempo))
print('Valor da prestação R${:.2f}'.format(prestação))
print('Seu limite R${:.2f}'.format(limite))
if prestação <= limite:
    print('\033[34mAPROVADO\033[m')
else:
    print('\033[31mREPROVADO\033[m')
