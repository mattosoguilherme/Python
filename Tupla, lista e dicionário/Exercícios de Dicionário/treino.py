# Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6,
# 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes
# aos quadrados desses números.
# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}

from typing import List


numeros=dict()

for c in range(1,10):
    if c==3 or c==2 or c==8:
        continue
    numeros[c]= c**2  

print('1º Exercício.')
print(numeros)
print('=-'*60)
print()
# 2. Exercício Treino - Crie um dicionário em que suas chaves correspondem a números
# inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

nm=dict()
for x in range(1,11):
    nm[x]=x**2
print(nm)
