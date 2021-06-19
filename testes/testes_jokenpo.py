print('''
                                                             JO KEN PO

         No inicio de tudo houve uma explosão que criou o uinverso como conhecemos hoje, e junto com o Big bang surgiram três
    poderes imensuráveis, são eles: O poder terra que controla todo material rochoso existente, o poder metal que controla todo
    material de ferro no universo e o poder folha que controla cada planta da flora universal.
         Esses poderes vieram parar em nosso planeta após milênios vagando nos confins do cósmos. No acaso do destino Três guerreiros 
    encontraram esses poderes: Jo, o destemido encontrou o poder terra, Ken, o Sevéro encontrou o poder metal e Po, o justo encontrou o poder planta.
    Eles eram chefes de tribos diferentes que estavam lutando para tomar o controle do território, mas não queriam uma guerra, pois
    sabiam que iriam derramar muito sangue inocente e como haviam se tornado detentores de um enorme poder lhes veio um grande senso de responsabilidade.
         Então decidiram realizar um torneio entre eles, quem vencesse iria se torna Rei de todo o território e os perdedores iriam ter 
    dois caminhos a seguir ou se jutarão ao novo rei e o apoirão ou levarão toda a sua tribo para outras terras...
    
''')
regras='''- O torneio de Jo, Ken e Pô está preste a começar, mas antes vamos as regras:
   1º Você deve escolher quantos rounds quer batalhar.
   2º Escolha um guerreiro, lembrando que:
   -Jo, representa o poder Terra;
   -Ken, representa o poder Metal;
   -Po, representa o poder folha. 
   3º Se divirta '''
while True:
   print(regras)
   rounds=int(input('Quantos rounds você quer jogar? '))
   guerreiro=input('Qual guerreiro é você? ').upper()
   guerreiro[0-1]
   if guerreiro==guerreiro:
       break
   else:
     print('Inválido')
     break
print(guerreiro)
print(rounds)


   

   
   
