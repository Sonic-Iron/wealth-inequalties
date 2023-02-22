"""
This is a cool document
"""
from GameInstance import run_sim


def main():
    """
    main
    :return: None
    """
    run_sim(num_players=32, tax_rate=0.02, num_rounds=5000)


if __name__ == "__main__":
    main()
