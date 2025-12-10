from itertools import combinations

filename = "dayA.txt"
with open(filename, "r") as f:
    lines = [[item for item in line.strip().split(" ")] for line in f.readlines()]


def check_target_reached(target, buttons, step):
    buttons_combinations = combinations(buttons, step)
    for buttons_combination in buttons_combinations:
        if [sum(item) % 2 for item in zip(*buttons_combination)] == target:
            return True
    return False


symbol_to_value = {"#": 1, ".": 0}
fewest_steps = []
for line in lines:
    target_configuration = [symbol_to_value[item] for item in list(line[0][1:-1])]
    buttons = [
        tuple(int(index) for index in item[1:-1].split(",")) for item in line[1:-1]
    ]

    buttons_configurations = []
    for button in buttons:
        button_configuration = [0] * len(target_configuration)
        for i in range(len(target_configuration)):
            if i in button:
                button_configuration[i] = 1
        buttons_configurations.append(button_configuration)

    target_reached = False
    fewest_step = 0
    while not target_reached:
        fewest_step += 1
        target_reached = check_target_reached(
            target_configuration, buttons_configurations, fewest_step
        )
    fewest_steps.append(fewest_step)

print(sum(fewest_steps))
