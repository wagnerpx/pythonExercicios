print('Saiba quantos litros de tinta vai precisar para \npintar sua casa, digite as informações logo abaixo:')
print('=' * 45)
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

# print('Processando as medidas {} X {} \nárea útil total {}m².'.format(lar, alt, (lar*alt)))
# print('Você vai precisar de {}l de tinta.'.format((lar*alt)/2))

print(f'Processando as medidas {lar} X {alt} \nárea útil total {lar*alt}m².')
print(f'Você vai precisar de {(lar*alt)/2}l de tinta.')
print('=' * 45)
