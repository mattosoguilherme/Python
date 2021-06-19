#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

num=list()
while True:
    nº1=int(input('digite um nº: '))
    if nº1 not in num:
        num.append(nº1)
    rsp=input('vc quer continuar?[S/N] ').strip().upper()[0]
    if rsp == 'N':
        break
num.sort()
print(f"\nsua lista: {num}\n\n")
print('-='*30)

# 2 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

numero=list()
impares=list()
pares=list()

while True: #laço infinito 
    nº=int(input('\ndigite um nº: '))
    numero.append(nº)
    if nº % 2 == 0: # isso é a mesma coisa que: se o resto da divisão da var 'nº' por dois for zero excecute a função abaixo.
        pares.append(nº) # esta função está add o vlr atual da var 'nº' dentro da lista da var 'pares'.
    else:
        impares.append(nº) # obs importante! Esta função (append) só deve ser utilizada com listas.
    rsp=input('vc quer continuar?[S/N] ').strip().upper()[0]

    if rsp == 'N':# condição criada para intenrromper o laço.
        break 
print(f'\nnº da sua lista:{numero}')
print(f'nº pares da sua lista:{pares}')
print(f'nº impares da sua lista:{impares}')
print()#pra pular linha 
print('-='*30)

# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
print()

from random import randint 
from time import sleep


jogos=list()
quant=int(input('Quantos jogos você quer? '))

for c in range(quant):
    lista_temp=list()
    cont=0
    while True:
        num= randint(1,60)
        if num not in lista_temp:
            lista_temp.append(num)
            cont+=1
        if cont>=6:
            break
    lista_temp.sort()

    jogos.append(lista_temp[:])
print(f"\n----------{quant} jogos sendo sorteados----------")
print()
for l,e in enumerate(jogos):
    print(f"O {l}º jogo sorteado foi: {jogos}")
    sleep(1)




