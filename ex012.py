preco = float(input('Valor total da compra: '))
desc = preco - (preco * 5 / 100)
print('Com 5% de desconto, você pagara R$ {}.'.format(desc))
print('Você teve uma economia de R$ {}'.format(preco - desc))
