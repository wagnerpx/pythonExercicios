""" strip() elimina os espaços do início e fim da frase.
    upper() transforma todas as palavras em maiusculas.
    lower() transforma todas as palavras em minúsculas.
    count() conta ou compara as palavras.
    split() serve para dividir uma string em substrings, ou seja, em partes menores.
"""

nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print(f'Seu nome completo tem {(len(nome) - nome.count(" "))} letras')
sepa_nome = nome.split()
lista = sepa_nome
print(f'Primeiro nome é {sepa_nome[0]} e tem {len(sepa_nome[0])} letras.')
print(f'Seu nome completo tem {len(lista)} nome(s)')
