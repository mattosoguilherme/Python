class People:
    def __init__(self,name,age,weight):
        self.namePeople = name
        self.agePeople = age
        self.weightPeople = weight
    
    def comer(self,calorias):
        if self.agePeople >=30:
            self.weightPeople += calorias*2
            return self.weightPeople 
        else:
            self.weightPeople+= calorias
            return self.weightPeople 
    
    def malhar(self,malhação):
        if self.agePeople < 30:
            self.weightPeople -= malhação*2
            return self.weightPeople
        else:
            self.weightPeople -= malhação
            return self.weightPeople
    
    def mostradordados(self):
        return f""" 
        Name = {self.namePeople} 
        Age = {self.agePeople}
        Weight = {self.weightPeople}
        """

def linha():
    print()
    print('-='*30)
    print()

peopleOne = People('Yasmin',21,59.7)
peopleTwo =  People('Guilherme',32,100)

peopleOne.comer(10)
peopleOne.malhar(5)

peopleTwo.comer(10)
peopleTwo.malhar(5)

print(peopleOne.mostradordados())

print(peopleTwo.mostradordados())

linha()

# Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e 
# Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione 
# uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na 
# tela: "Você não tem saldo suficiente para essa operação."

class Account:
    def __init__(self,holder,balance):
        self.hoderAccount = holder
        self.balanceAccount = balance
    
    def moreMoney(self,deposit):
        self.balanceAccount += deposit
        return self.balanceAccount
    
    def lessmoney(self,):
        pass


