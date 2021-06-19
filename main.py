#Tuplas, lista (lista compostas), dicionários.

#sintaxes correta tupla() e lsta[]
 
# pessoas=('Ana','João','Guilherme','Thiago')

# for l in sorted(pessoas)[::-1]:
#  print(f'{l}\n')
# print('-='*20)

# from random import randint

# numero=(randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50))

# print(f'{sorted(numero)}\n')
# print(f'maior:{max(numero)}\nmenor:{min(numero)}')

# print('-='*20)

# vlr=(int(input('digite um numero: ')),int(input('digite um numero: ')),int(input('digite um numero: ')),int(input('digite um numero: ')))
# for n,c in enumerate(sorted(vlr)):
#     print(f'{n+1}º posição: {c}')
     
# print(f'\no numero 9 apareceu {vlr.count(9)} vezes')
  
#lista
 
#  função de lista:
#  append() |add um valor sempre na ultima posição
#  lista[] |substitui um valor de qualquer posição
#  list() |cria um lista
#  .insert(posição, valor) |insere um valor em qualquer posição
#  .remove() apaga qualquer valor dentro dentro de uma lista 
#  .pop() apaga uma posição específico dentro de uma lista, se estiver sem parâmetro ele apaga a ultima posição da lista 
#   .sort() | faz a mesma coisa que o sorted, coloca em ordem crescente
#   .reverse()| faz o inverso do sorted 
#  del.clear() | limpa uma lista

# Exercicios de Lista:

# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.
# l = [5, 7, 2, 9, 4, 1, 3]
# l.sort()
# print(f'\nlista:{l}\n')
# print(f' A lista tem {len(l)} números.')
# print(f'{max(l)} é o maior nº da lista')
# print(f'{min(l)} é o menor nº da lista')
# print(f'A soma de todos os nº da lista é {sum(l)}')
# print(f' lista em ordem crescente:\n{l}')
# l.reverse()
# print(f'lista em ordem decrescente:\n{l}')


# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

dtv=[input("Telefonou para a vítima?[S/N]\n").strip().capitalize()[0],input("Esteve no local do crime?[S/N]\n").strip().capitalize()[0], input("Mora perto da vítima?[S/N]\n").strip().capitalize()[0],input("Devia para a vítima?[S/N]\n").strip().capitalize()[0],input("Já trabalhou com a vítima?[S/N]\n").strip().capitalize()[0]]
ponto=0
for c in dtv:
    if c == 'S':
        ponto+=1
   
if ponto <=1:
    print("\nvc é inocente")
elif ponto == 2:
    print("\nvc é suspeito")
elif ponto==3 or ponto==4:
    print("\nvc é cumplice")
elif ponto==5:
    print("\nvc é culpado")
