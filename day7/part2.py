filename = "day7.txt"

with open(filename, "r") as f:
    lines = [line.strip() for line in f.readlines()]

# key is column and value is number of timelines
splitter_columns = {lines[0].index("S"): 1}

for line in lines[1:]:
    splitter_columns_updated = {}
    for splitter_column in splitter_columns.keys():
        if line[splitter_column] == "^":
            splitter_columns_updated[splitter_column - 1] = (
                splitter_columns_updated.get(splitter_column - 1, 0)
                + splitter_columns[splitter_column]
            )
            splitter_columns_updated[splitter_column + 1] = (
                splitter_columns_updated.get(splitter_column + 1, 0)
                + splitter_columns[splitter_column]
            )
        else:
            splitter_columns_updated[splitter_column] = (
                splitter_columns_updated.get(splitter_column, 0)
                + splitter_columns[splitter_column]
            )
    splitter_columns = splitter_columns_updated

print(sum(splitter_columns.values()))
