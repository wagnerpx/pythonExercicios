km = float(input('Kilometros percorrido KM: '))
dia = int(input('Dias utilizado: '))
diaria = (dia * 60) + (km * 0.15)
print(f'você utilizou {dia} dias e rodou {km}Km')
print(f'O valor a pagar é R${diaria:.2f}')
