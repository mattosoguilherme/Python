
# 5. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
print("CADASTRO DE PESSOAS")
pessoas=[]
povo={}
soma=media=0
print()
while True:
    povo["nome"]=str(input('Digite o nome: ').capitalize().strip())
    povo["sexo"]=str(input(f'Sexo biológico de {povo["nome"]}:[F/M] ')).strip().upper()[0]
    while povo["sexo"] not in "FM":
        print("RESPONDA APENAS F ou M!")
        povo["sexo"]=str(input(f'Sexo biológico de {povo["nome"]}:[F/M] ')).strip().upper()[0]

    povo["idade"]=int(input(f'Digite a idade de {povo["nome"]}:'))
    soma+=povo["idade"]
    pessoas.append(povo.copy())
    p=input('Dejesa cadastrar mais alguém? [S/N] ').strip().upper()[0]
    while p not in "SN":
        print("RESPONDA S OU N!porfavor")
        p=input('Dejesa cadastrar mais alguém? [S/N] ').strip().upper()[0]       
    if p=='N':
        break
    if p=='S':
        continue
media= soma/len(pessoas)
Mulheres=[]
for i in pessoas:
    if i["sexo"]=="F":
        Mulheres.append(i['nome'])
acima=list()
for a in pessoas:
    if a['idade']>media:
        acima.append(a['idade'])

print("-"*30 )

print(f"Você cadastrou o total de {len(pessoas)} pessoas.")
print(f"A média da idade dessas pessoas é {media} anos. ")
print(f"Existem {len(Mulheres)} na lista, são elas:",end=" ")
for t in Mulheres:
    print(t, end=',')
print(f"\nIdades acima da média são:{acima}.")






   

