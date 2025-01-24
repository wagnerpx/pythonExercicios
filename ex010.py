print(f'{" CASA DE CAMBIO VIRTUAL ":=^44}')
real = float(input('Qual valor você deseja converter? R$ '))
dolar = real / 5.90
euro = real / 6.19
libra = real / 7.37
peso = real / 0.005741
print('=' * 52)
print(f'Com R${real} você pode comprar (Dólar)US${dolar:.2f}')
print(f'Com R${real} você pode comprar (EURO)EUR${euro:.2f}')
print(f'Com R${real} você pode comprar (LIBRA)GBP${libra:.2f}')
print(f'Com R${real} você pode comprar (PESO)ARS${peso:.2f}')
print('=' * 52)
