from day2.utils import *


def main(lines: list[str]):
    games: list[Game] = []
    rounds: list[Round] = []
    read_data(games, rounds, lines)

    testcase = {"red": 12, "green": 13, "blue": 14}
    result: int = 0
    for game in games:
        not_found = False
        for key in testcase:
            if key not in game.cubes:
                not_found = True
                break
            if game.cubes[key] > testcase[key]:
                not_found = True
                break
        if not_found is True:
            continue
        result += game.ID

    return result
