import random

players = []
num_players = 2
num_rounds = 1000
num_transactions_PRound = 1
PercentWagedLarge = 0.2
PercentWagedSmall = 0.17
LargeBias = 0.1

starting_wealth = 200


class Player:
    def __init__(self, ID, wealth):
        self.ID = ID
        self.wealth = wealth

    def lose(self, wtl):
        self.wealth -= wtl

    def win(self, wtw):
        self.wealth += wtw
def generateplayers():
    for x in range(num_players):
        players.append(Player(len(players), starting_wealth))


def runtransaction(players):
    P1 = random.choice(players)
    P2 = P1
    while(P2==P1):
        P2 = random.choice(players)
    if random.randint(0,1):

def main():
    generateplayers()
    runtransaction(players)



if __name__ == "__main__":
    main()
