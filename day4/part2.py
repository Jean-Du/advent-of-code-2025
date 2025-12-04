import numpy as np

filename = "day4.txt"

symbol_to_value = {"@": 1, ".": 0}

list_of_lines = []
with open(filename, "r") as f:
    for line in f:
        list_of_lines.append([symbol_to_value[item] for item in list(line.strip())])

initial_array = np.array(list_of_lines)
number_of_movable_rolls = 0


def count_movable_rolls(raw_array):
    padded_array = np.pad(raw_array, ((1, 1), (1, 1)))

    roll_pairs = [
        (x_roll, y_roll) for x_roll in range(-1, 2) for y_roll in range(-1, 2)
    ]
    roll_pairs.remove((0, 0))

    rolled_arrays = []

    for roll_pair in roll_pairs:
        rolled_arrays.append(
            np.roll(np.roll(padded_array, roll_pair[0], axis=0), roll_pair[1], axis=1)
        )

    summed_array = np.sum(rolled_arrays, axis=0)[1:-1, 1:-1]
    potential_movable_array = summed_array < 4
    real_movable_array = potential_movable_array & raw_array

    return real_movable_array.sum(), raw_array - real_movable_array


rolls_removed_each_round, updated_array = count_movable_rolls(initial_array)
number_of_movable_rolls += rolls_removed_each_round
while rolls_removed_each_round != 0:
    rolls_removed_each_round, updated_array = count_movable_rolls(updated_array)
    number_of_movable_rolls += rolls_removed_each_round

print(number_of_movable_rolls)
