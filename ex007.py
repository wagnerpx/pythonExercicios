print('========= Avaliação Bimestral =========')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
str = 'Media'
print('{:=^40}'.format(str))
print('Primeira nota: {:.1f} \nSegunda nota: {:.1f} '.format(n1, n2))
print('============ Nota Final ===========')
print('A média foi: {:.1f}'.format((n1+n2)/2))
