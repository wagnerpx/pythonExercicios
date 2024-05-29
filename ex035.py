print('\033[32m-=-=\033[m' * 10)
print('Analisador de Triângulos')
print(('\033[32m-=-=\033[m' * 10))
r1 = float(input('Primeiro segmento:'))
r2 = float(input('segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m triângulo!')
else:
    print('Os segmentos acima \033[34mPODEM FORMAR\033[m triângulo!')
