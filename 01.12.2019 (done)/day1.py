# --- Day 1: The Tyranny of the Rocket Equation ---
# Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately
# calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs
# you to bring him measurements from fifty stars.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
# puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# The Elves quickly load you into a spacecraft and prepare to launch.

# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount
# of fuel required yet.

# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module
# , take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fue
# l needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?


def get_input_from_file():
    file = open('/Users/piotrkuk/Documents/git-repos/advent/01.12.2019 (done)/dataInput.txt', 'r')
    return file.read().replace('\n', ' ').split(' ')


def count_fuel(module_weight):
    div = module_weight / 3
    return int(div) - 2


def count_fuel_all(module_weight):
    single_module_fuel_weight_complete = 0
    temp = module_weight
    while single_module_fuel_weight_complete >= 0:
        single_module_fuel_weight = count_fuel(temp)
        single_module_fuel_weight_complete = single_module_fuel_weight_complete + single_module_fuel_weight
        temp = single_module_fuel_weight
        if single_module_fuel_weight / 3 - 2 <= 0:
            break

    print(str(single_module_fuel_weight_complete))
    return single_module_fuel_weight_complete


def calculate_all(list_of_values):
    full_module_fuel = 0
    for v in list_of_values:
        module_weight = int(v)
        single_module_fuel_weight_complete = count_fuel_all(module_weight)
        full_module_fuel = full_module_fuel + single_module_fuel_weight_complete
    return full_module_fuel


# TESTS
assert count_fuel(12) == 2, "should be 2"
assert count_fuel(14) == 2, "should be 2"
assert count_fuel(1969) == 654, "should be 654"
assert count_fuel(100756) == 33583, "should be 33583"

assert count_fuel_all(14) == 2, "should be 2"
assert count_fuel_all(1969) == 966, "should be 966"
assert count_fuel_all(100756) == 50346, "should be 50346"

values = get_input_from_file()
print(calculate_all(values))
