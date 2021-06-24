def linha():
    print('-='*30)
# 1Faça um programa, com uma função que necessite de um parametro. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def sinal(n):
    if n>0:
        return "P"
    if n<=0:
        return  "N"


num=sinal(int(input('digite um número: ')))
print(num)

linha()
# 2 Faça um programa em Python com uma função que necessite de três parametros, e que forneça: 
# # A soma desses três parametros através de uma função. # Seu script também deve fornecer a 
# média dos três números, através de uma segunda função que chama a primeira.

def calculador(n,n2,n3):
    n=n+n2+n3
    return n  
def media(n4):
    m=n4/3
    return m

top=calculador(9,3,6)
l=media(top)
print(l)