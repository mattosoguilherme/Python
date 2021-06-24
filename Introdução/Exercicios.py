def linhas():
    print("-="*30)
#1-Letra de música - Faça um programa que mostre na tela uma letra de música que você gosta (proibido letras do Justin Bieber).
print("""Olha que coisa mais linda mais cheia de graça
É ela menina que vem e que passa
No doce balanço, a caminho do mar""")
linhas()
#4-Tabela de notas - Você foi contratado ou contratada por uma escola pra fazer o sistema de boletim dos alunos.
#  Como primeiro passo, escreva um programa que produza a seguinte saída:
# ALUNO (A)  NOTA
# =========  ====
# ALINE      9.0
# MÁRIO      DEZ
# SÉRGIO     4.5
# SHIRLEY    7.0
def calculadorMedia(a,b):
    media=a/b
    return media
boletin={}
alunos=[]
media_notas=[]
qtd_alunos=0
while True:
    boletin['Aluno']=str(input("Nome do Aluno(a): ")).capitalize().strip()
    qtd_alunos+=1
    boletin["Nota da Prova"]=float(input("Digite a nota da prova: "))
    media_notas.append(boletin["Nota da Prova"])
    alunos.append(boletin.copy())
    p=input('Dejesa incluir mais algum aluno(a)? [S/N] ').strip().upper()[0]
    while p not in "SN":
        print("RESPONDA S OU N!porfavor")
        p=input('Dejesa incluir mais algum aluno(a)? [S/N] ').strip().upper()[0]       
    if p=='N':
        break
    if p=='S':
        continue

print('''RESULTADO PROVAS FINAIS=== 
ALUNOS(AS)  NOTAS''')
for k,v in enumerate(alunos):
    for f in v.values():
        print(f'{f} ', end="     ")
    print()
if len(media_notas)>1:
    print(f'A média de nota geral: {calculadorMedia(sum(media_notas),qtd_alunos)}')
print(f'Maior nota da turma: {max(media_notas)}')