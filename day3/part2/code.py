symbol = '*'


def search_for_number(line: str, index: int):
    number = ''
    # Search if the number continues on the left side of the index
    for i in range(index, -1, -1):
        if line[i].isdigit():
            number += line[i]
        else:
            break
    # Reverse the number
    number = number[::-1]

    # Search if the number continues on the right side of the index
    for i in range(index + 1, len(line)):
        if line[i].isdigit():
            number += line[i]
        else:
            break

    return int(number)


def check_around_gear(line: int, index: int, lines: list[str]) -> int:
    number_of_digits: int = 0
    numbers: list[int] = []
    # Check if the previous character is a digit
    if index > 0:
        if lines[line][index - 1].isdigit():
            number_of_digits += 1
            numbers.append(search_for_number(lines[line], index - 1))

    # Check if the next character is a digit
    if index < len(lines[line]) - 1:
        if lines[line][index + 1].isdigit():
            number_of_digits += 1
            numbers.append(search_for_number(lines[line], index + 1))

    if line > 0:
        found_number = False
        # Check if the character in upper left is a digit
        if index > 0:
            if lines[line - 1][index - 1].isdigit():
                number_of_digits += 1
                found_number = True
                numbers.append(search_for_number(lines[line - 1], index - 1))

        # Check if the character above is a digit
        if lines[line - 1][index].isdigit() and not lines[line - 1][index - 1].isdigit():
            number_of_digits += 1
            if not found_number:
                numbers.append(search_for_number(lines[line - 1], index))

        # Check if the upper middle character is not a digit
        # This is to avoid be able to count two numbers in the same line
        if not lines[line - 1][index].isdigit():
            found_number = False

        # Check if the character in upper right is a digit
        if index < len(lines[line - 1]) - 1:
            if lines[line - 1][index + 1].isdigit() and not lines[line - 1][index].isdigit():
                number_of_digits += 1
                if not found_number:
                    numbers.append(search_for_number(lines[line - 1], index + 1))

    if line < len(lines) - 1:
        found_number = False
        # Check if the character in lower left is a digit
        if index > 0:
            if lines[line + 1][index - 1].isdigit():
                number_of_digits += 1
                found_number = True
                numbers.append(search_for_number(lines[line + 1], index - 1))

        # Check if the character below is a digit
        if lines[line + 1][index].isdigit() and not lines[line + 1][index - 1].isdigit():
            number_of_digits += 1
            if not found_number:
                numbers.append(search_for_number(lines[line + 1], index))

        # Check if the lower middle character is not a digit
        # This is to avoid be able to count two numbers in the same line
        if not lines[line + 1][index].isdigit():
            found_number = False

        # Check if the character in lower right is a digit
        if index < len(lines[line - 1]) - 1:
            if lines[line + 1][index + 1].isdigit() and not lines[line + 1][index].isdigit():
                number_of_digits += 1
                if not found_number:
                    numbers.append(search_for_number(lines[line + 1], index + 1))

    # Check if there are two numbers around the gear
    if number_of_digits == 2:
        return numbers[0] * numbers[1]
    else:
        return -1


def main(lines: list[str]):
    _sum: int = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            # Check if the current position is a gear
            if lines[i][j] == symbol:
                aux = check_around_gear(i, j, lines)
                if aux != -1:
                    _sum += aux

    return _sum
