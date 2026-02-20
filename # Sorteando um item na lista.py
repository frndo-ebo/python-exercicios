# Sorteando um item na lista
import random

al1=input('Digite o nome do/a primeiro/a aluno/a:')
al2=input('Digite o nome do/a segundo/a aluno/a:')
al3=input('Digite o nome do/a terceiro/a aluno/a:')
al4=input('Digite o nome do/a quarto/a aluno/a:') 
lista=[al1, al2, al3, al4]

sort=random.choice(lista)
print(f'O aluno/a sorteado/a foi: {sort}')