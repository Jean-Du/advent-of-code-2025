import math

filename = "day6.txt"

with open(filename, "r") as f:
    raw_lines = f.readlines()

number_lines = [line.removesuffix("\n") for line in raw_lines[:-1]]
operation_line = raw_lines[-1]
operation_columns = []
for position, content in enumerate(operation_line):
    if content != " ":
        operation_columns.append(position)
operation_columns.append(max(len(number_line) for number_line in number_lines))


def do_math(operation, numbers):
    if operation == "+":
        return sum(numbers)
    elif operation == "*":
        return math.prod(numbers)


total_sum = 0
for operation_count, operation_column in enumerate(operation_columns[:-1]):
    operation = operation_line[operation_column]
    numbers = []
    for number_column in range(
        operation_column, operation_columns[operation_count + 1]
    ):
        number_string = "".join(
            [
                number_line[number_column]
                for number_line in number_lines
                if len(number_line) > number_column
            ]
        ).strip()
        if number_string:
            numbers.append(int(number_string))
    total_sum += do_math(operation, numbers)

print(total_sum)
