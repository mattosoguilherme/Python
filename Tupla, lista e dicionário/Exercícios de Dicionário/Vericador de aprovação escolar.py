# 3. Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.

escola=dict()
print('Verificador de aprovação escolar')
print()
escola['aluno']=str(input('nome: ')).strip().upper()
escola['média']=int(input(f"média do {escola['aluno']}:[0-10] "))
print()
if escola['média']>=7:
    escola['situação']='APROVADO'
if 5>= escola['média']<=6.9:
    escola['situação']='RECUPERAÇÃO'
if escola['média']<=4.9:
    escola['situação']='REPROVADO'

for i,s in enumerate  (escola):
    print(f"{s}:{escola[s]}")
