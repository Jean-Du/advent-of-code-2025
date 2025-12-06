import math

filename = "day6.txt"

with open(filename, "r") as f:
    raw_lines = f.readlines()
    operations = [symbol for symbol in raw_lines[-1].strip().split(" ") if symbol != ""]
    lines = [
        [int(num) for num in line.strip().split(" ") if num != ""]
        for line in raw_lines[:-1]
    ]

total_sum = 0
for pos, operation in enumerate(operations):
    if operation == "+":
        total_sum += sum([column for column in [line[pos] for line in lines]])
    elif operation == "*":
        total_sum += math.prod([column for column in [line[pos] for line in lines]])

print(total_sum)
