"""
Runs a yard sale simulation
"""
import random
import numpy as np


class Player:
    """
    Represents a player, all values of wealth inside are decimal and returns Decimal type to outside the instance
    """
    def __init__(self, wealth):
        """
        Create a player
        :param wealth: the player's wealth
        """
        self.wealth = wealth


def generate_players(count, wealth):
    """
    Generates a pool of players
    :param count: the number of players
    :param wealth: the starting wealth of each player
    :return: list of Player()
    """
    return [Player(wealth) for _ in range(count)]


def run_round(p1, p2, large_bias, small_wager, large_wager):
    """
    Run a round of the game
    :param p1: the list of players, len >= 2
    :param large_bias: The percent of time the wealthier player will win
    :param small_wager: The percent won/lost when the poorer player wins
    :param large_wager: The percent won/lost when the richer player wins
    """
    p_more, p_less = ((p1, p2) if p1.wealth >= p2.wealth else (p2, p1))
    if np.random.binomial(1, 0.5 + large_bias):
        # the wealthier player wins
        wager = int(p_less.wealth * small_wager)
        p_more.wealth += wager
        p_less.wealth -= wager
    else:
        wager = int(p_less.wealth * large_wager)
        p_less.wealth += wager
        p_more.wealth -= wager


def generate_pairs(players):
    permutation = np.random.permutation(players)
    for i in range(0, len(players), 2):
        yield permutation[i], permutation[i+1]


def main():
    """
    Runs the game
    """
    num_players = 64
    num_rounds = 1000
    large_wager = 0.2
    small_wager = 0.17
    large_bias = 0.01
    starting_wealth = 200000

    players = generate_players(num_players, starting_wealth)

    for a in range(num_rounds):
        for p1, p2 in generate_pairs(players):
            run_round(p1, p2, large_bias, small_wager, large_wager)
        total_wealth = 0
        for b in players:
            total_wealth += b.wealth
        print("round", a, [p.wealth for p in players], total_wealth)


if __name__ == "__main__":
    main()
