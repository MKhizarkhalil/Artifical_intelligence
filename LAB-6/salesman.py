from itertools import permutations

vertices = ["1", "2", "3", "4"]

routes = [
    ["1", "2", 10],
    ["1", "4", 20],
    ["1", "3", 15],
    ["2", "4", 25],
    ["2", "3", 35],
    ["3", "4", 30],
]

adjacencyList = {}


def addVertex(vertex):
    adjacencyList[vertex] = []


def addEdges(dest1, dest2, weight):
    adjacencyList[dest1].append([dest2, weight])
    adjacencyList[dest2].append([dest1, weight])


for i in vertices:
    addVertex(i)

for i in routes:
    addEdges(*i)


def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        current_city = path[i]
        next_city = path[i + 1]
        for neighbor, weight in adjacencyList[current_city]:
            if neighbor == next_city:
                cost += weight
                break
    # Add the cost to return to the starting vertex
    start_city = path[0]
    last_city = path[-1]
    for neighbor, weight in adjacencyList[last_city]:
        if neighbor == start_city:
            cost += weight
            break
    return cost


def find_minimum_cost_cycle(start_vertex):
    min_cost = float('inf')
    best_path = []

    vertices_to_permute = vertices.copy()
    vertices_to_permute.remove(start_vertex)

    for perm in permutations(vertices_to_permute):
        current_path = [start_vertex] + list(perm) + [start_vertex]
        current_cost = calculate_cost(current_path)
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path

    return best_path, min_cost


# Example usage:
start_vertex = "1"
best_path, min_cost = find_minimum_cost_cycle(start_vertex)
print("Minimum weight:", min_cost)
print(f"Sequence: {best_path}")
