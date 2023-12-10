from day4.common_utils import *


def main(lines: list[str]):
    cards: list[Card] = []
    read_data(cards, lines)
    total_number_of_cards: int = 0
    for index in range(1, len(cards)):
        wins_on_card: int = cards[index].count_numbers()
        # print("Card " + str(index) + " wins on " + str(wins_on_card) + " numbers")
        for index_next in range(1, wins_on_card + 1):
            # print(f"Next card: {index + index_next}")
            cards[index + index_next].instances += cards[index].instances
        total_number_of_cards += cards[index].instances

    print("Total number of cards: " + str(total_number_of_cards))
    return total_number_of_cards
