num = int(input('Informe um número até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
if u == 0:
    print('Não tem Unidade')
elif u >= 1:
    print(f'Unidade {u}')
if d == 0:
    print('Não tem Dezena')
elif d >= 1:
    print(f'Dezena {d}')
if c == 0:
    print('Não tem Centena')
elif c >= 1:
    print(f'Centena {c}')
if m == 0:
    print('Não tem Milhar')
elif m >= 1:
    print(f'Milhar {m}')
