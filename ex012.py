preco = float(input('Valor total da compra: '))
desc = preco - (preco * 5 / 100)

print('=' * 45)
print(f'Com 5% de desconto, você ira pagar R$ {desc}')
print(f'Você teve uma economia de R$ {(preco-desc):.2f}')
print('=' * 45)
