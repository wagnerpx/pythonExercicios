nome = 'Wagner Alexandre Peixoto da Silva'
print('Transformando o nome com UPPER\n', nome.upper())
print('Transformando o nome com lower\n', nome.lower())
espaco = nome.replace(' ', '')
letras = len(espaco.strip())
print('Seu nome completo tem {} letras'.format(letras))
primeiro = nome.split()
print('Seu primeiro nome é {}'.format(primeiro[0]))
print('O nome {} tem {} letras.'.format(primeiro[0], len(primeiro[0][0:])))
