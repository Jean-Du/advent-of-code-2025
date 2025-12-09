filename = "day9.txt"

with open(filename, "r") as f:
    red_tiles = [
        tuple(int(coordinate) for coordinate in line.strip().split(","))
        for line in f.readlines()
    ]

largest_area = 0
for i, red_tile_a in enumerate(red_tiles):
    for red_tile_b in red_tiles[i + 1 :]:
        area = (abs(red_tile_a[0] - red_tile_b[0]) + 1) * (
            abs(red_tile_a[1] - red_tile_b[1]) + 1
        )
        if area > largest_area:
            largest_area = area

print(largest_area)
