soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c:2}° número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Vc digitou {cont} números pares, \nA soma deles é {soma}')
