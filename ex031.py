km = float(input('Qual é a distancia da sua viagem: '))

print('\033[33m=\033[m' * 40)
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.40
print(f'Sua viagem vai custar R$ {preço}')
print('\033[33m=\033[m' * 40)
