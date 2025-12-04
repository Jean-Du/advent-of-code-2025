import numpy as np

filename = "day4.txt"

symbol_to_value = {"@": 1, ".": 0}

list_of_lines = []
with open(filename, "r") as f:
    for line in f:
        list_of_lines.append([symbol_to_value[item] for item in list(line.strip())])

raw_array = np.array(list_of_lines)
padded_array = np.pad(raw_array, ((1, 1), (1, 1)))

roll_pairs = [(x_roll, y_roll) for x_roll in range(-1, 2) for y_roll in range(-1, 2)]
roll_pairs.remove((0, 0))

rolled_arrays = []

for roll_pair in roll_pairs:
    rolled_arrays.append(
        np.roll(np.roll(padded_array, roll_pair[0], axis=0), roll_pair[1], axis=1)
    )

summed_array = np.sum(rolled_arrays, axis=0)[1:-1, 1:-1]
mark_movable_array = summed_array < 4
final_array = mark_movable_array & raw_array

print(final_array.sum())
