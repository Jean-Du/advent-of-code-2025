filename = "day3.txt"

list_of_lines = []
with open(filename, "r") as f:
    for line in f:
        list_of_lines.append([int(item) for item in list(line.strip())])

list_of_max_values = []
for line in list_of_lines:
    first_digit = max(line[:-1])
    first_digit_index = line.index(first_digit)
    second_digit = max(line[first_digit_index + 1 :])
    list_of_max_values.append(first_digit * 10 + second_digit)

print(list_of_max_values)
print(sum(list_of_max_values))
