filename = "day1.txt"

dial_number = 50
counter = 0

with open(filename, "r") as f:
    for line in f:
        start = dial_number
        rotation = int(line.replace("L", "-").replace("R", "+"))
        full_rotation, remainder = divmod(abs(rotation), 100)
        counter += full_rotation
        if remainder == 0:
            continue
        if rotation < 0:
            remainder = -remainder
        end = start + remainder
        if (end >= 100 or end <= 0) and (start != 0):
            counter += 1
        dial_number = end % 100


# with open (filename, "r") as f:
#     for line in f:
#         start=dial_number
#         rotation=int(line.replace("L","-").replace("R","+"))
#         end=dial_number+rotation
#         if rotation > 0:
#             for i in range(start+1,end+1):
#                 if i % 100 == 0:
#                     counter += 1
#         if rotation < 0:
#             for i in range(end, start):
#                 if i % 100 == 0:
#                     counter += 1
#         dial_number=end%100

print(counter)
