"""
Runs a yard sale simulation
"""
import random
import numpy as np


class Player:
    """
    Represents a player
    """
    def __init__(self, wealth):
        """
        Create a player
        :param wealth: the player's wealth
        """
        self._wealth = wealth

    def get_wealth(self):
        return self._wealth

    def lose(self, loss):
        """
        :param loss: how much wealth was lost
        """
        self._wealth -= loss

    def win(self, gain):
        """
        :param gain: how much wealth was won
        """
        self._wealth += gain


def generate_players(count, wealth):
    """
    Generates a pool of players
    :param count: the number of players
    :param wealth: the starting wealth of each player
    :return: list of Player()
    """
    return [Player(wealth) for _ in range(count)]


def run_round(players, large_bias, small_wager, large_wager):
    """
    Run a round of the game
    :param players: the list of players, len >= 2
    :param large_bias: The percent of time the wealthier player will win
    :param small_wager: The percent won/lost when the poorer player wins
    :param large_wager: The percent won/lost when the richer player wins
    """
    players_temp = players[:]
    for _ in range(len(players)//2):
        p1, p2 = random.sample(players_temp, 2)
        players_temp.remove(p1)
        players_temp.remove(p2)
        print(len(players_temp))
        if np.random.binomial(1, large_bias):
            # the wealthier player wins
            if p1.get_wealth() >= p2.get_wealth():
                p1.win(p2.get_wealth()*small_wager)
                p2.lose(p2.get_wealth()*small_wager)
            else:
                p2.win(p1.get_wealth()*large_wager)
                p1.lose(p1.get_wealth()*large_wager)
        else:
            # the poorer player wins
            if p1.get_wealth() >= p2.get_wealth():
                p1.lose(p2.get_wealth()*large_wager)
                p2.win(p2.get_wealth()*large_wager)
            else:
                p1.win(p1.get_wealth()*large_wager)
                p2.lose(p1.get_wealth()*large_wager)

def main():
    """
    Runs the game
    """
    num_players = 100
    num_rounds = 10000
    large_wager = 0.2
    small_wager = 0.17
    large_bias = 0.5 + 0.01
    starting_wealth = 200

    players = generate_players(num_players, starting_wealth)

    for a in range(num_rounds):
        print("round", a)
        run_round(players, large_bias, small_wager, large_wager)
        total_wealth = 0
        for a in players:
            total_wealth += a.get_wealth()
        print(total_wealth)



if __name__ == "__main__":
    main()
