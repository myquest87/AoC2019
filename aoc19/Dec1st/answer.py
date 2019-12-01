from pathlib import Path
import numpy as np

input_path = Path(__file__).parent.joinpath("input.txt")


def _get_fuel_required(module_mass: int):
    return np.floor(module_mass / 3) - 2


def main():
    with input_path.open() as input_file:
        total_fuel_required = 0
        for module_mass in input_file:
            module_mass_as_int = int(module_mass)

            fuel_required_for_module = _get_fuel_required(module_mass_as_int)

            total_fuel_required += fuel_required_for_module
        print(total_fuel_required)


if __name__ == "__main__":
    main()
