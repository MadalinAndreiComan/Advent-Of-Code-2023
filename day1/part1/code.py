def main(lines: list[str]):
    _sum = 0
    for line in lines:
        number = 0
        for i in range(len(line)):
            if line[i].isdigit():
                number = int(line[i])
                break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                number = number * 10 + int(line[i])
                break

        _sum += number
    return _sum
