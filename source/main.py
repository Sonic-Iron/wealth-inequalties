"""
This is a cool document
"""
from GameInstance import run_sim


def main():
    """
    main
    :return: None
    """
    #large_wager_array = [0.2, 0.21, 0.25]
    #small_wager_array = [0.17, 0.17, 0.1]
    #large_bias_array = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
    #for i in range(len(large_wager_array)):
     #   for j in range(len(large_bias_array)):
      #      run_sim(large_wager=large_wager_array[i], small_wager=small_wager_array[i], large_bias=large_bias_array[j])
    run_sim(num_players=2)


if __name__ == "__main__":
    main()
