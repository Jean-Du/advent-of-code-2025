import math

filename = "day8.txt"

with open(filename, "r") as f:
    junctions = [
        [int(coordinate) for coordinate in line.strip().split(",")]
        for line in f.readlines()
    ]


number_of_shortest_distances_required = 1000
shortest_distances = [((-1, -1), math.inf)] * number_of_shortest_distances_required
for i, junction_a in enumerate(junctions[:-1]):
    for j, junction_b in enumerate(junctions[i + 1 :]):
        distance = math.dist(junction_a, junction_b)
        if distance > shortest_distances[0][1]:
            continue
        elif (
            distance <= shortest_distances[number_of_shortest_distances_required - 1][1]
        ):
            shortest_distances.append(((i, j + i + 1), distance))
            shortest_distances.pop(0)
        else:
            for k, shortest_distance in enumerate(shortest_distances[1:]):
                if distance > shortest_distance[1]:
                    shortest_distances.insert(k + 1, ((i, j + i + 1), distance))
                    shortest_distances.pop(0)
                    break

circuits = []
for connected_pair, _ in shortest_distances:
    connected = False
    connected_pair_set = set(connected_pair)
    for i, circuit_a in enumerate(circuits):
        if connected_pair_set & circuit_a:
            circuit_a.update(connected_pair_set)
            connected = True
            for j, circuit_b in enumerate(circuits[i + 1 :]):
                if connected_pair_set & circuit_b:
                    circuit_a.update(circuit_b)
                    circuits.pop(j + i + 1)
                    break
            break
    if not connected:
        circuits.append(connected_pair_set)

circuit_lengths = sorted([len(circuit) for circuit in circuits], reverse=True)
print(math.prod(circuit_lengths[0:3]))
