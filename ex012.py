preco = float(input('Valor total da compra: '))
desc = preco - (preco * 5 / 100)
print('=' * 45)
print('Com 5% de desconto, você irá pagar R$ {}.'.format(desc))
print('Você teve uma economia de R$ {:.2f}'.format(preco - desc))
print('=' * 45)
