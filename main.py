from utils import *
import day2.utils as current_day
import day2.part1.code as first_part
import day2.part2.code as second_part


def main():
    day_name: str = current_day.get_name()

    part1_example: str = read_file(f"{day_name}/part1/input/input.example")
    part1_test: str = read_file(f"{day_name}/part1/input/input.test")
    part2_example: str = read_file(f"{day_name}/part2/input/input.example")
    part2_test: str = read_file(f"{day_name}/part2/input/input.test")

    part1_output_example = first_part.main(part1_example.splitlines()) if part1_example != "" else ""
    part1_output = first_part.main(part1_test.splitlines()) if part1_test != "" else ""
    part2_output_small = second_part.main(part2_example.splitlines()) if part2_example != "" else ""
    part2_output = second_part.main(part2_test.splitlines()) if part2_test != "" else ""

    write_file(f"{day_name}/part1/output/output.example", part1_output_example)
    write_file(f"{day_name}/part1/output/output.test", part1_output)
    write_file(f"{day_name}/part2/output/output.example", part2_output_small)
    write_file(f"{day_name}/part2/output/output.test", part2_output)


if __name__ == '__main__':
    main()
