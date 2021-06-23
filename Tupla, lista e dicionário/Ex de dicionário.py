
# Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6,
# 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes
# aos quadrados desses números.
# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}

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
print()
print('=-'*60)
print()

# 3. Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.

escola=dict()
print('Verificador de aprovação')
print()
escola['aluno']=str(input('nome: ')).strip().upper()
escola['média']=int(input(f"média do {escola['aluno']}: "))
print()
if escola['média']>=7:
    escola['situação']='APROVADO'
if 5>= escola['média']<=6.9:
    escola['situação']='RECUPERAÇÃO'
if escola['média']<=4.9:
    escola['situação']='REPROVADO'

for i,s in enumerate  (escola):
    print(f"{s}:{escola[s]}")

print()
print('=-'*60)
print()

# PARTE1- Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário.
# PARTE2- Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.
# PARTE3- Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. 
# PARTE4- Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
print('CALCULADOR DE APOSENTADORIA')
print()
inss=dict()
inss['nome']=input('Digite seu nome: ').capitalize()
inss['Nascimento']=2021-int(input('Qual seu ano de nascimento? '))
inss['ctps']=int(input('Qual nº da sua carteira de trabalho? Se não possui digite "0". '))

if inss['ctps']!=0:
    inss['contribuição']=int(input('Em que ano você foi contratado? '))
    inss['slr']=float(input('Qual seu salário? '))

inss['beneficio'] = 2021 - inss['contribuição']
print()
if inss['beneficio'] <35:
    inss['beneficio'] = 35-(2021 - inss['contribuição'])
    print(f"{inss['nome']} tem {inss['Nascimento']} anos de idade, falta {inss['beneficio']} anos para ele(a) se aposentar.")

if inss['beneficio'] >35:
    print(f"{inss['nome']} já está aposentado")
print()




