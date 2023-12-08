class Round:
    def __init__(self):
        self.cubes = {}

    def add_another_round(self, nr, color):
        if color not in self.cubes:
            self.cubes[color] = nr
        else:
            self.cubes[color] += nr


class Game:
    def __init__(self, index):
        self.ID: int = int(index)
        self.cubes = {}


def read_data(games: list[Game], rounds: list[Round], lines: list[str]):
    for line in lines:
        games.append(Game(line.split(":")[0].split(" ")[1]))
        for element in line.split(": ")[1].split("; "):
            rounds.append(Round())
            for item in element.split(", "):
                rounds[-1].add_another_round(int(item.split(" ")[0]), item.split(" ")[1].replace("\n", ""))
            for key in rounds[-1].cubes:
                if key not in games[-1].cubes:
                    games[-1].cubes[key] = rounds[-1].cubes[key]
                if rounds[-1].cubes[key] > games[-1].cubes[key]:
                    games[-1].cubes[key] = rounds[-1].cubes[key]
