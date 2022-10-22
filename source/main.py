"""
Runs a yard sale simulation
"""
import random


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


def run_round(players):
    """
    Run a round of the game
    :param players: the list of players, len >= 2
    """
    p1, p2 = random.sample(players, 2)

    # TODO: replace with random distribution code


def main():
    """
    Runs the game
    """
    num_players = 2
    num_rounds = 1000
    # transactions_per_round = 1
    # large_wager = 0.2
    # small_wager = 0.17
    # large_bias = 0.1
    starting_wealth = 200

    players = generate_players(num_players, starting_wealth)

    for _ in range(num_rounds):
        run_round(players)


if __name__ == "__main__":
    main()
