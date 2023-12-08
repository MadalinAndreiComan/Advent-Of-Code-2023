from utils import *


def main():
    day_path, day_exec = get_day_info()

    example: str = read_file(f"{day_path}/input/input.example")
    test: str = read_file(f"{day_path}/input/input.test")

    example_output = day_exec.main(example.splitlines()) if example != "" else ""
    test_output = day_exec.main(test.splitlines()) if test != "" else ""

    print(f"\nExample output: {example_output}")
    print(f"Test output: {test_output}")
    write_file(f"{day_path}/output/output.example", example_output)
    write_file(f"{day_path}/output/output.test", test_output)


if __name__ == '__main__':
    main()
