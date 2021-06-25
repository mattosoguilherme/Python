def linha():
    print()
    print('-='*30)
# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a
# soma desses três argumentos.
def somador(a,b,c):         
    u=a+b+c
    return u

# 2. Faça um programa, com uma função que necessite de um argumento. A função retorna
# o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for
# negativo e ‘0’ se for 0.

def apurate(d):
    if d>0:
        return "Positivo"
    if d<0:
        return "Negativo"
    if d==0:
        return "Neutro"

print(f'''O nº 1 é {apurate(1)}'
O nº 0 é {apurate(0)}
O nº -1 é {apurate(-1)} ''')
linha()
#3. Faça um programa com uma função chamada somaImposto. A função possui dois
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o
# valor de custo para incluir o imposto sobre vendas.

def  somaImposto(taxaImposto,custo):
    taxa=taxaImposto/100
    impost=custo+(custo*taxa)
    return impost

print(somaImposto(38,100))
linha()
# 4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário
# é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha
# mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas
def salariador(h_trab):
    float(h_trab)
    if h_trab<=40:  
        slr= h_trab*6.8875
    else:
        h_exced=h_trab-40
        slr= (40*6.8875+ (h_exced*1.5))
        slr=f"{slr:,.2f}"
        slr= slr.replace(",","_")
        slr= slr.replace(".",",")
        slr= slr.replace("_",".")
    return f"R$ {slr}"

print(salariador(100))
linha()
#5-Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
def imcdor(peso,altura):
    calculo=peso/altura**2
    calculo=f'{calculo:.2f}'
    return calculo

print(imcdor(75,1.68))
linha()
#6. Escreva uma função que, dado um número nota representando a nota de um estudante,
# converte o valor de nota para um conceito (A, B, C, D, E e F).
# Nota Conceito
# >=9.0 A
# >=8.0 B
# >=7.0 C
# >=6.0 D
# <=4.0 F

def notador(n):
    if n >=9:
        x="A"
    elif n>=8:
        x="B"
    elif n>=7:
        x="C"
    elif n>=6:
        x="D"
    elif n>=5:
        x="E"
    elif n<=4:
        x="f"
    return x

print(f''' Notas  =  Repres.
    9.0    {notador(9)}
    8.0    {notador(8) }     
    7.0    {notador(7)}
    6.0    {notador(6)}
    5.0    {notador(5)}
    4.0    {notador(4)} (e demais notas abaixo de 4.0)
''')
linha()
# 7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles
# forem iguais, imprima que eles são iguais.
def adicionador(f,g):
    h=[]
    h.append(f)
    h.append(g)
    if f ==g:
        return h
    else:
        return min(h)

print(adicionador(100,100))
linha()
print("FIM")