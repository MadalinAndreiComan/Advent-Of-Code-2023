symbols = ['+', '-', '*', '/', '#', '$', '%', '&', '@', '!', '?', '^', '~', '<', '>', '=', ':', ';', '|']


def add_number(start_index: int, end_index: int, line: str):
    number = ''
    for i in range(start_index, end_index):
        number += line[i]
    return int(number)


def check_around_number(start_index: int, end_index: int, line: int, lines: list[str]):
    # Check if the next character is a symbol
    if end_index < len(lines[line]):
        if lines[line][end_index] in symbols:
            return True

    # Check if the previous character is a symbol
    if start_index > 0:
        if lines[line][start_index - 1] in symbols:
            return True

    if line > 0:
        # Check if the character in upper left is a symbol
        if start_index > 0:
            if lines[line - 1][start_index - 1] in symbols:
                return True
        # Check if the character in upper right is a symbol
        if end_index < len(lines[line - 1]) - 1:
            if lines[line - 1][end_index] in symbols:
                return True
        # Check if any of the characters in the line above are symbols
        for i in range(start_index, end_index):
            if lines[line - 1][i] in symbols:
                return True

    if line < len(lines) - 1:
        # Check if the character in lower left is a symbol
        if start_index > 0:
            if lines[line + 1][start_index - 1] in symbols:
                return True
        # Check if the character in lower right is a symbol
        if end_index < len(lines[line - 1]) - 1:
            if lines[line + 1][end_index] in symbols:
                return True
        # Check if any of the characters in the line below are symbols
        for i in range(start_index, end_index):
            if lines[line + 1][i] in symbols:
                return True

    return False


def main(lines: list[str]):
    is_number: bool = False
    _sum: int = 0
    start_of_number: int = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):

            # Check if the character is a number
            if lines[i][j].isdigit() and is_number is False:
                start_of_number = j
                is_number = True
                continue

            # Check if the character is a symbol
            if not lines[i][j].isdigit() and is_number is True:
                if check_around_number(start_of_number, j, i, lines):
                    _sum += add_number(start_of_number, j, lines[i])
                is_number = False

            # Check if the character is a number and it's the last character in the line
            if j == len(lines[i]) - 1 and is_number is True:
                if check_around_number(start_of_number, j + 1, i, lines):
                    _sum += add_number(start_of_number, j + 1, lines[i])
                is_number = False

    return _sum
