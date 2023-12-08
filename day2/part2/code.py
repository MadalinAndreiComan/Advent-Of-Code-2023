from day2.common_utils import *


def main(lines: list[str]):
    games: list[Game] = []
    rounds: list[Round] = []
    read_data(games, rounds, lines)

    power: int
    result: int = 0
    for game in games:
        power = 1
        for value in game.cubes.values():
            power *= value
        result += power
    return result
