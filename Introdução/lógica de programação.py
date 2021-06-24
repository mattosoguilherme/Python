def linhas():
    print()
    print("-="*30)
#01 - Elabore um programa que imprima na tela a seguinte frase Olá Mundo! Esse é o meu primeiro programa.
programador=input('nome:').capitalize().strip()
print(f"{programador}:\n-Hello word! This is my first program.")
linhas()
#02 - Elabore um programa que escreve seu nome completo na primeira linha, seu endereço na segunda e o CEP  na terceira.
cadastro={}
cadastro['nome']=input("Nome: ").capitalize().strip()
cadastro['endereço']=input("Endereço: ").capitalize().strip()
cadastro['cep']=input("CEP: ")
print("-"*15)
print("==CADASTRO ENDEREÇO==")
for k,v in cadastro.items():
  print(f"{k}= {v}")
linhas()
#03 - Elabore um programa que recebe o nome de uma pessoa do terminal e mostra a seguinte mensagem: Olá {nome}! Seja bem vindo ao 
# fantástico mundo da programação.
usuário=input('DIGITE SEU NOME: ').capitalize().strip()
print(f"Hello {usuário}! Welcome to fantastic world of programation.")
linhas()
#04 - Elabore um programa que recebe dois valores inteiros e mostra a soma desses valores
def somador(a,b):
    return a+b
print("=CALCULADORA EM APRENDIZADO: SOMA APENAS DOIS VALORES INTEIROS=")
print(f'Resultado da soma = {somador(int(input("Digite um nº: ")),int(input("Digite um nº: ")))} ')
linhas()
#05 - Elabore um programa que receba 4 notas de um aluno e calcule a média dele.
boletin=[]
for n in range(4):
    notas=float(input(f'{n+1}º nota: '))
    boletin.append(notas)
media=sum(boletin)/4
print(f"Média do aluno é {media}")
linhas()
#06 - Elabore um programa que recebe dois valores inteiros e mostra se o primeiro valor é maior ou igual ao segundo valor
n1=int(input("Digite um nº: "))
n2=int(input("Digite um nº: "))
resultado=n1>=n2
print(f"{usuário}:\n- Is the firt number greater than the second?\nComputer:\n-{resultado}")