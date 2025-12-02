filename = "day2.txt"


def find_invalid_ids(min_id, max_id):
    invalid_ids = []

    for number_of_repeats in range(2, len(str(max_id)) + 1):

        min_length_div, min_length_mod = divmod(len(str(min_id)), number_of_repeats)
        if min_length_mod != 0:
            temp_min_id = int(
                "1" + "0" * ((min_length_div + 1) * number_of_repeats - 1)
            )
        else:
            temp_min_id = min_id

        max_length_div, max_length_mod = divmod(len(str(max_id)), number_of_repeats)
        if max_length_mod != 0:
            temp_max_id = int("9" * max_length_div * number_of_repeats)
        else:
            temp_max_id = max_id

        if temp_max_id >= temp_min_id:
            temp_max_id_first_part = int(
                str(temp_max_id)[: int(len(str(temp_max_id)) / number_of_repeats)]
            )
            if temp_max_id >= int(str(temp_max_id_first_part) * number_of_repeats):
                max_repeat_unit = temp_max_id_first_part
            else:
                max_repeat_unit = temp_max_id_first_part - 1

            temp_min_id_first_part = int(
                str(temp_min_id)[: int(len(str(temp_min_id)) / number_of_repeats)]
            )
            if temp_min_id <= int(str(temp_min_id_first_part) * number_of_repeats):
                min_repeat_unit = temp_min_id_first_part
            else:
                min_repeat_unit = temp_min_id_first_part + 1

            invalid_ids.extend(
                int(str(repeat_unit) * number_of_repeats)
                for repeat_unit in range(min_repeat_unit, max_repeat_unit + 1)
            )

    invalid_ids_unique = list(set(invalid_ids))
    return invalid_ids_unique


with open(filename, "r") as file:
    file_content = file.read()
    range_strings = file_content.split(",")

invalid_ids_in_given_ranges = []
for range_string in range_strings:
    range_start = int(range_string.split("-")[0])
    range_end = int(range_string.split("-")[1])
    invalid_ids_in_given_ranges.extend(find_invalid_ids(range_start, range_end))

invalid_ids_sum = sum(invalid_ids_in_given_ranges)
# print(invalid_ids_in_given_ranges)
print(invalid_ids_sum)
