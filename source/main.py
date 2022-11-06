"""
This is a cool document
"""
from GameInstance import run_sim


def main():
    """
    main
    :return: None
    """
    for u in range(100, 10000):
        for i in range(0, 100):
            for j in range(0, 100):
                for k in range(-50, 50):
                    run_sim(num_rounds=u,
                            large_wager=(i/100),
                            small_wager=(j/100),
                            large_bias=(k/100))
                    print(u, i, j, k)


if __name__ == "__main__":
    main()
