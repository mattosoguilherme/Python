# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula
# anterior, crie um lançador de dados e moedas em que o usuário deve
# escolher o objeto a ser lançado. Não esqueça que os lançamentos são
# feitos de forma randômica.
from random import randint
from os import system


class Launcher:
   
    def __init__(self,object):
        self.die_or_coin = object
        if object == "dado":
            self.die_or_coin = randint(1,6)
            return print(self.die_or_coin)
        if object == "moeda":
            self.die_or_coin = randint(0,1)
            if self.die_or_coin == 0 :
                self.die_or_coin = 'cara'
            else:
                self.die_or_coin = 'coroa'
            return print(self.die_or_coin)
    
   

Launcher(input("qual objeto você quer jogar? [dado ou moeda] "))
system('clear')
# Vamos aprimorar o código: cadastro de jogador de futebol.py que foi
# desenvolvido no Code Lab da aula 14. Faça com que o seu código
# funcione para vários jogadores, incluindo um sistema de visualização de
# detalhes de aproveitamento de cada jogador.

#01 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.

class Player:
    def __init__(self,name,team,match):   
        self.player_library=dict()
        self.player_library["Player"] = name
        self.player_library["Team"] = team
        self.player_library["number_match"] = match     
        self.all_goals = list()
        for count in range(match):
            self.number_goals = int(input(f"Quantos gols {name} fez nessa {count+1}º partida?\n "))
            self.all_goals.append(self.number_goals)

    def players_income(self):
        print('-- PLAYER INCOME --')
        for keys, values in self.player_library.items():
            print(f"{keys}: {values}")
        all = sum(self.all_goals)
        average = all / self.player_library["number_match"]
        print(f"Total of goals: {all}")
        print(f"Average goals per game: {average}")

while True:
    athlete = Player(input("Qual o nome do jogador?\n").capitalize(),
    input("Qual o time?\n").capitalize(),
    int(input("Quantas partidas jogou?\n"))
    )
    system('clear')

    athlete.players_income()
    question = input('')
