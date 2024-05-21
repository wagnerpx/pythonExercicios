lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print('Uma parede {} X {} tem uma área de {} M²'.format(lar, alt, (lar*alt)))
print('Precisamos de {} latas de tinta.'.format((lar*alt)/2))
