import heapq
import sys

# Distance Matrix
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

num_cities = len(distance_matrix)
start_city = 0

def get_heuristic(current_city, unvisited, matrix):
    if not unvisited:
        return matrix[current_city][start_city]

    heuristic = min(matrix[current_city][u] for u in unvisited)

    for u in unvisited:
        targets = [v for v in unvisited if v != u]
        targets.append(start_city)
        heuristic += min(matrix[u][v] for v in targets)

    return heuristic

def solve_tsp_astar(matrix, start):
    pq = []

    unvisited = set(range(num_cities))
    unvisited.remove(start)

    h = get_heuristic(start, unvisited, matrix)
    heapq.heappush(pq, (h, start, [start], 0))

    while pq:
        f, current, path, g = heapq.heappop(pq)

        print("Current Path:", path, "Cost:", g)

        if len(path) == num_cities:
            total_cost = g + matrix[current][start]
            return path + [start], total_cost

        for next_city in range(num_cities):
            if next_city not in path:
                new_g = g + matrix[current][next_city]
                remaining = set(range(num_cities)) - set(path) - {next_city}
                new_h = get_heuristic(next_city, remaining, matrix)
                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (new_f, next_city, path + [next_city], new_g)
                )

    return [], sys.maxsize

# Main Program
print("Travelling Salesman Problem using A* Search\n")

route, cost = solve_tsp_astar(distance_matrix, start_city)

print("\nOptimal Route:")
print(" -> ".join("City {}".format(i) for i in route))
print("Minimum Cost:", cost)
