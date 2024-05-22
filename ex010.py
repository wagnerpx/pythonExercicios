real = float(input('Qual valor você deseja converter? R$ '))
dolar = real / 5.10
euro = real / 5.54
libra = real / 6.48
peso = real / 0.005741
print('=' * 52)
print('Com R${} você pode comprar (Dólar)US${:.2f}'.format(real, dolar))
print('Com R${} você pode comprar (EURO)EUR${:.2f}'.format(real, euro))
print('Com R${} você pode comprar (LIBRA)GBP${:.2f}'.format(real, libra))
print('Com R${} você pode comprar (PESO)ARS${:.2f}'.format(real, peso))
print('=' * 52)
