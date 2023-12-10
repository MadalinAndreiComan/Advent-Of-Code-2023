class Card:
    def __init__(self):
        self.winning_numbers = []
        self.my_numbers = []
        self.instances = 1

    def add_winning_numbers(self, winning_numbers):
        self.winning_numbers.append(winning_numbers)

    def add_my_numbers(self, my_numbers):
        self.my_numbers.append(my_numbers)

    def count_numbers(self) -> int:
        count: int = 0
        for number in self.my_numbers:
            if number in self.winning_numbers:
                count += 1
        return count

    def count_points(self):
        count = 0
        for number in self.my_numbers:
            if number in self.winning_numbers:
                if count == 0:
                    count = 1
                else:
                    count *= 2
        return count


def read_data(cards: list[Card], lines: list[str]):
    cards.append(Card())
    for line in lines:
        cards.append(Card())
        for number in line.split(": ")[1].split(" | ")[0].split(" "):
            if number == '':
                continue
            cards[-1].add_winning_numbers(int(number))
        for number in line.split(":")[1].split(" | ")[1].split(" "):
            if number == '':
                continue
            cards[-1].add_my_numbers(int(number))
