dist = float(input('Distancia em metros: '))
print('Convertendo {:=^20}'.format(dist))
print('|', (dist / 1000), 'Km')
print('|', (dist / 100), 'Hm')
print('|', (dist / 10), 'Dam')
print('|', (dist * 10), 'dm')
print('|', (dist * 100), 'cm')
print('|', (dist * 1000), 'mm')
print('v')