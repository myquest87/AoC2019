from pathlib import Path
import numpy as np

input_path = Path(__file__).parent.joinpath("input.txt")


def _get_fuel_required(mass: int):
    return np.floor(mass / 3) - 2


def _get_answer_part_1():
    # answer is 3367126
    with input_path.open() as input_file:
        total_fuel_required = 0
        for module_mass in input_file:
            module_mass_as_int = int(module_mass)

            fuel_required_for_module = _get_fuel_required(module_mass_as_int)

            total_fuel_required += fuel_required_for_module
    return total_fuel_required


def _get_answer_part_2():
    # answer is 5047796
    with input_path.open() as input_file:
        total_fuel_required = 0
        for module_mass in input_file:
            module_mass_as_int = int(module_mass)
            fuel_required_for_module = _get_fuel_required(module_mass_as_int)

            fuel_required_for_fuel = _get_fuel_required(fuel_required_for_module)
            fuel_required_for_module += fuel_required_for_fuel

            while fuel_required_for_fuel > 0:
                fuel_required_for_fuel = _get_fuel_required(fuel_required_for_fuel)
                if fuel_required_for_fuel > 0:
                    fuel_required_for_module += fuel_required_for_fuel

            total_fuel_required += fuel_required_for_module
    return total_fuel_required


def main():
    answer = _get_answer_part_2()
    print(answer)


if __name__ == "__main__":
    main()
