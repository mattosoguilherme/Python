# PARTE1- Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário.
# PARTE2- Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.
# PARTE3- Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. 
# PARTE4- Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
print('CALCULADOR DE APOSENTADORIA')
print()
inss=dict()
inss['nome']=input('Digite seu nome: ').capitalize()
inss['idade']=2021-int(input('Qual seu ano de nascimento? '))
inss['ctps']=int(input('Qual nº da sua carteira de trabalho? Se não possui digite "0". '))
if inss["ctps"]==0:
    print('-'*30)
    for k,v in inss.items():
        print(f'{k}= {v}')
    
if inss['ctps']!=0:
    inss['contribuição']=int(input('Em que ano você foi contratado? '))
    inss['slr']=float(input('Qual seu salário? '))
    inss['beneficio'] = 2021 - inss['contribuição']
    print()
    if inss['beneficio'] <35:
        inss['beneficio'] = 35-(2021 - inss['contribuição'])
        print(f"{inss['nome']} tem {inss['idade']} anos de idade, falta {inss['beneficio']} anos para ele(a) se aposentar.")

    if inss['beneficio'] >35:
        print(f"{inss['nome']} já está aposentado ou já pode se aposentar")
