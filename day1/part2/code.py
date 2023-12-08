digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def main(lines: list[str]):
    _sum: int = 0
    for line in lines:
        first_digit: int = 0
        second_digit: int = 0
        for i in range(len(line)):

            if line[i].isalpha():
                aux: int = 0
                if line[i: i + 3] in digits.keys():
                    aux = digits[line[i: i + 3]]
                elif line[i: i + 4] in digits.keys():
                    aux = digits[line[i: i + 4]]
                elif line[i: i + 5] in digits.keys():
                    aux = digits[line[i: i + 5]]

                if aux == 0:
                    continue

                if first_digit == 0:
                    first_digit = aux

                second_digit = aux
                continue

            if line[i].isdigit():
                if first_digit == 0:
                    first_digit = int(line[i])
                second_digit = int(line[i])

        number = first_digit * 10 + second_digit
        _sum += number
    return _sum
