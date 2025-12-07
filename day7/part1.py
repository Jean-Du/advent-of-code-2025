filename = "day7.txt"

with open(filename, "r") as f:
    lines = [line.strip() for line in f.readlines()]

splitter_counter = 0
splitter_columns = [lines[0].index("S")]

for line in lines[1:]:
    splitter_columns_updated = []
    for splitter_column in splitter_columns:
        if line[splitter_column] == "^":
            splitter_columns_updated.extend([splitter_column - 1, splitter_column + 1])
            splitter_counter += 1
        else:
            splitter_columns_updated.append(splitter_column)
    splitter_columns = list(set(splitter_columns_updated))

print(splitter_counter)
