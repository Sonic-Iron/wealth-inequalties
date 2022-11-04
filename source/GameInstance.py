"""
Runs a yard sale simulation
"""
import csv
import os
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
    :param p1: the first player in the transaction
    :param p2: the second player in the transaction
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
    """
    A function to generate a pair of players out of the total group of players uniquely.
    :param players:
    :return:
    """
    permutation = np.random.permutation(players)
    for i in range(0, len(players), 2):
        yield permutation[i], permutation[i+1]


def generate_gini_coefficient(starting_wealth, row):
    """
    A function to generate a gini coefficient for a given set of values
    :param starting_wealth: the wealth each player starts with in each run
    :param row: The set of data to gind the gini coefficient for
    :return: returns the coefficient
    """
    row = sorted(row)
    max_area = 0.5
    wealth_area = 0
    for p in range(len(row)):
        area_set = row[0:p+1]
        wealth_area += ((area_set.pop()/(starting_wealth*len(row)))/len(row))/2
        wealth_area += (sum(area_set)/(starting_wealth*len(row)))/len(row)
    return (max_area-wealth_area)/max_area


def main():
    """
    Runs the game
    """
    num_players = 4
    num_rounds = 10000
    large_wager = 0.20
    small_wager = 0.17
    large_bias = 0
    starting_wealth = 2000000

    players = generate_players(num_players, starting_wealth)
    add = 0
    while True:
        if os.path.isfile(
                './' + str(num_players) + str(num_rounds) + str(large_wager) + str(small_wager) + str(large_bias) + str(starting_wealth)+"N"+ str(add)):
            add += 1
            continue
        break
    for a in range(num_rounds):
        for p1, p2 in generate_pairs(players):
            run_round(p1, p2, large_bias, small_wager, large_wager)
        total_wealth = 0
        for b in players:
            total_wealth += b.wealth
        with open('./'+str(num_players)+str(num_rounds)+str(large_wager)+str(small_wager)+str(large_bias)+str(starting_wealth)+"N"+str(add), 'a', newline="") as f:
            writer = csv.writer(f)
            row_data = [p.wealth for p in players]
            row_data.append(generate_gini_coefficient(starting_wealth, row_data))
            writer.writerow(row_data)
            f.close()
        print("round", a, [p.wealth for p in players], total_wealth)


if __name__ == "__main__":
    main()
