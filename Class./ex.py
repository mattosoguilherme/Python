# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula
# anterior, crie um lançador de dados e moedas em que o usuário deve
# escolher o objeto a ser lançado. Não esqueça que os lançamentos são
# feitos de forma randômica.
from random import randint

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
        self.list_player_library = list()    
        self.player_library=dict()
        self.player_library["namePlayer"] = name
        self.player_library["nameTeam"] = team
        self.player_library["number_match"] = match 
        self.list_player_library.append(self.player_library.copy())
        self.all_goals = list()
        for count in range(match):
            self.number_goals = input(f"Quantos gols {name} fez nessa {count+1}º partida?\n ")  
            self.all_goals.append(self.number_goals)
   
    def players_income():
        pass


print()
Player(input("Qual o nome do jogador?\n").capitalize(),
input("Qual o time?\n").capitalize(),
int(input("Quantas partidas jogou?\n"))
)
