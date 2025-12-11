filename = "dayB.txt"

with open(filename, "r") as f:
    lines = {
        line.strip().split(": ")[0]: line.strip().split(": ")[1].split(" ")
        for line in f.readlines()
    }

global_path_counter = 0


def recursive_find_out(input_device, devices_configuration, used_devices):
    global global_path_counter
    for output_device in devices_configuration[input_device]:
        if output_device == "out":
            global_path_counter += 1
        elif output_device not in used_devices:
            path_used_devices = used_devices + [output_device]
            recursive_find_out(output_device, devices_configuration, path_used_devices)

    return None


recursive_find_out("you", lines, ["you"])
print(global_path_counter)
