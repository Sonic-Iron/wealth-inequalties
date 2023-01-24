"""
Runs a yard sale simulation
"""
import csv
import os
import sys
import time
import warnings

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


def run_transaction(p1, p2, large_bias, small_wager, large_wager, np_gen):
    """
    Run a round of the game
    :param p1: the first player in the transaction
    :param p2: the second player in the transaction
    :param large_bias: The percent of time the wealthier player will win
    :param small_wager: The percent won/lost when the poorer player wins
    :param large_wager: The percent won/lost when the richer player wins
    :param np_gen: the variable to use for random generation using the same seed
    """
    p_more, p_less = ((p1, p2) if p1.wealth >= p2.wealth else (p2, p1))
    if np_gen.binomial(1, 0.5 + large_bias):
        # the wealthier player wins
        wager = int(p_less.wealth * small_wager)
        p_more.wealth += wager
        p_less.wealth -= wager
    else:
        # the poorer player wins
        wager = int(p_less.wealth * large_wager)
        p_less.wealth += wager
        p_more.wealth -= wager


def generate_pairs(players, np_gen):
    """
    A function to generate a pair of players out of the total group of players uniquely
    :param players: the list of players
    :param np_gen: the random number seed to use to generate permutations of players
    :return:
    """
    permutation = np_gen.permutation(players)
    for i in range(0, len(players), 2):
        yield permutation[i], permutation[i + 1]


def generate_gini_coefficient(starting_wealth, row):
    """
    A function to generate a Gini coefficient for a given set of values
    :param starting_wealth: the wealth each player starts with in each run
    :param row: The set of data to find the Gini coefficient for
    :return: returns the coefficient
    """
    row = sorted(row)
    max_area = 0.5
    wealth_area = 0
    for v in range(len(row)):
        area_set = row[0:v + 1]
        wealth_area += ((area_set.pop() / (starting_wealth * len(row))) / len(row)) / 2
        wealth_area += (sum(area_set) / (starting_wealth * len(row))) / len(row)
    return (max_area - wealth_area) / max_area


def valid_check(num_players, num_rounds, large_wager, small_wager, large_bias):
    if num_players % 2:
        sys.exit("Number of players has to be a multiple of 2")
    if num_rounds < 0:
        sys.exit("The number of rounds needs to be positive")
    if not 0 <= large_wager <= 1:
        warnings.warn("Large Wager needs to be between 0 and 1")
        large_wager = np.clip(large_wager, 0, 1)
    if not 0 <= small_wager <= 1:
        warnings.warn("Small Wager needs to be between 0 and 1")
        small_wager = np.clip(small_wager, 0, 1)
    if not -0.5 <= large_bias <= 0.5:
        warnings.warn("The large bias needs to be between -0.5 and 0.5")
        large_bias = np.clip(large_bias, -0.5, 0.5)
    return large_wager, small_wager, large_bias


def run_round(large_bias, small_wager, large_wager, starting_wealth, players, writer, np_gen, tax_rate):
    for p1, p2 in generate_pairs(players, np_gen):
        run_transaction(p1, p2, large_bias, small_wager, large_wager, np_gen)
    redistribute(players, tax_rate)
    row_data = [p.wealth for p in players]
    row_data.append(generate_gini_coefficient(starting_wealth, row_data))
    writer.writerow(row_data)
    return False


def redistribute(players, tax_rate):
    tax_refund = (sum([player.wealth for player in players]) * tax_rate) / len(players)
    for player in players:
        player.wealth *= (1 - tax_rate)
        player.wealth += tax_refund


def run_sim(num_players=2,
            num_rounds=1000,
            large_wager=0.2,
            small_wager=0.17,
            large_bias=0,
            starting_wealth=2000000,
            random_seed=1,
            tax_rate=0):
    """
    Runs the game
    :param num_players: The default number of players per game
    :param num_rounds:  The default  number of rounds per game
    :param large_wager: The default  large wager of a game
    :param small_wager: The default  small wager of a game
    :param large_bias: The default  bias towards the richer player of a game
    :param starting_wealth: The default  starting wealth per player of a game
    :param random_seed: The default seed of randomness, so that different games can be compared
    :param tax_rate: The percent of tax paid by each actor
    :return: None
    """
    np_gen = np.random.default_rng(seed=random_seed)
    large_wager, small_wager, large_bias = valid_check(num_players, num_rounds, large_wager, small_wager, large_bias)
    players = generate_players(num_players, starting_wealth)
    add = 0
    while True:
        if os.path.isfile(
                './' + str(num_players) + str(num_rounds) + str(large_wager) +
                str(small_wager) + str(large_bias) + str(starting_wealth) + "N" + str(add)):
            add += 1
            continue
        break
    with open('./' + str(num_players) + str(num_rounds) + str(large_wager) +
              str(small_wager) + str(large_bias) + str(starting_wealth) + "N" + str(add), 'a+', encoding='utf-8',
              newline="") as f:
        writer = csv.writer(f)
        for _ in range(num_rounds):
            if run_round(large_bias, small_wager, large_wager, starting_wealth, players, writer, np_gen, tax_rate):
                break
        f.seek(0)
        reader = csv.reader(f)
        g_i = ''
        pos = 1
        for row in reader:
            g_i += '(' + str(pos) + ',' + str(round(float(row[2]), 4)) + ')'
            pos += 1
        print(g_i)
        f.close()


if __name__ == "__main__":
    run_sim()
