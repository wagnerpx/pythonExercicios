print('\n')
nome = input('Nome do Funcionário(a):')
sal = float(input('Salário R$: '))
reaj = float(input('Reajuste (%): '))
valor = (reaj * sal)/100
nsal = sal + valor
print('\n\n')
print('=' * 60)
print('O(a) funcionário(a): \n{}, ganhava R$ {}'.format(nome, sal))
print('e depois de ganhar um reajuste de {}% de aumento.'.format(reaj))
print('vai ter um aumento de R$ {} no salário.'.format(valor))
print('vai passar a ganhar R$ {}.'.format(nsal))
print('=' * 60)
