from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
esclhido = choice(lista)
print(f'O(a) aluno(a) escolhido(a) foi :{esclhido}')
