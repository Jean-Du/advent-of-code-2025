filename = "day2.txt"


def find_invalid_ids(min_id, max_id):
    invalid_ids = []

    if len(str(min_id)) % 2 == 1:
        min_id = int("1" + "0" * len(str(min_id)))

    if len(str(max_id)) % 2 == 1:
        max_id = int("9" * (len(str(max_id)) - 1))

    if max_id >= min_id:
        max_id_first_half = int(str(max_id)[: int(len(str(max_id)) / 2)])
        max_id_second_half = int(str(max_id)[int(len(str(max_id)) / 2) :])
        if max_id_first_half > max_id_second_half:
            max_repeat_unit = max_id_first_half - 1
        else:
            max_repeat_unit = max_id_first_half
        min_id_first_half = int(str(min_id)[: int(len(str(min_id)) / 2)])
        min_id_second_half = int(str(min_id)[int(len(str(min_id)) / 2) :])
        if min_id_first_half < min_id_second_half:
            min_repeat_unit = min_id_first_half + 1
        else:
            min_repeat_unit = min_id_first_half
        invalid_ids.extend(
            int(str(repeat_unit) * 2)
            for repeat_unit in range(min_repeat_unit, max_repeat_unit + 1)
        )

    return invalid_ids


with open(filename, "r") as file:
    file_content = file.read()
    range_strings = file_content.split(",")

invalid_ids_in_given_ranges = []
for range_string in range_strings:
    range_start = int(range_string.split("-")[0])
    range_end = int(range_string.split("-")[1])
    invalid_ids_in_given_ranges.extend(find_invalid_ids(range_start, range_end))

invalid_ids_sum = sum(invalid_ids_in_given_ranges)
print(invalid_ids_in_given_ranges)
print(invalid_ids_sum)
