filename = "day3.txt"
batteries_needed_each_line = 12


def find_max_digit(
    list_of_numbers,  # truncated list
    digit_position,
    total_number_of_digits=batteries_needed_each_line,
):
    if digit_position == total_number_of_digits:
        max_digit = max(list_of_numbers[:])
    else:
        max_digit = max(list_of_numbers[: -(total_number_of_digits - digit_position)])
    max_digit_index = list_of_numbers.index(max_digit)
    return max_digit, max_digit_index


list_of_lines = []
with open(filename, "r") as f:
    for line in f:
        list_of_lines.append([int(item) for item in list(line.strip())])

list_of_max_values = []
for line in list_of_lines:
    max_value_string = ""
    digit_index = -1
    for digit in range(1, batteries_needed_each_line + 1):
        max_digit_value, digit_index = find_max_digit(line, digit)
        max_value_string += str(max_digit_value)
        line = line[digit_index + 1 :]
    list_of_max_values.append(int(max_value_string))

print(list_of_max_values)
print(sum(list_of_max_values))
