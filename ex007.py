print(f'{" Notas Bimestral ":=^40}')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

print(f'{" Notas ":=^40}')
print(f'Primeira nota: {n1 :.1f} \nSegunda nota: {n2 :.1f} ')
print(f'{" Média Final ":=^40}')
print(f'A média foi: {(n1+n2)/2 :.1f}')
