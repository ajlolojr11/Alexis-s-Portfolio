# Cards Program Ver 1.0
import random

cards = ["jack", "queen", "king"]


def main():
    random.seed(0)
    # Testing choice(), choices(), sample()
    print(random.choices(cards, weights=[100, 0, 0], k=2))


if __name__ == "__main__":
    main()
