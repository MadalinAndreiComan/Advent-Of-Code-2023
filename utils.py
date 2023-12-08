import os.path
import sys
import importlib.util


def get_day_info() -> (str, any):
    # Here we ask the user for the day and part they want to see
    day_path = input("What day do you want to see?(1-25): ")
    while not day_path.isdigit() or int(day_path) < 1 or int(day_path) > 25:
        day_path = input("What day do you want to see?(1-25): ")

    part_name = input("What part do you want to see?(1-2): ")
    while not part_name.isdigit() or int(part_name) < 1 or int(part_name) > 2:
        part_name = input("What part do you want to see?(1-2): ")

    day_path = "./day" + day_path + "/part" + part_name

    # Here we import the code.py file from the day folder
    module_path = day_path + "/code.py"
    abs_module_path = os.path.abspath(module_path)
    sys.path.append(os.path.dirname(abs_module_path))
    spec = importlib.util.spec_from_file_location("code", abs_module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    # Here we return the path to the day folder and the module
    return day_path, module


def read_file(file: str):
    if not os.path.isfile(file):
        return ""

    with open(file, "r") as f:
        return f.read()


def write_file(file: str, data: any):
    with open(file, "w") as f:
        f.write(str(data))
