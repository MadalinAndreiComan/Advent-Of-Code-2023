from day4.common_utils import *


def main(lines: list[str]):
    cards: list[Card] = []
    read_data(cards, lines)

    _sum: int = 0
    # start from 1 to keep the card number identical with the index in the list
    for card in cards[1:]:
        _sum += card.count_points()

    return _sum
