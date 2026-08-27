from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == target or b == target:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        # Generate all possible next states
        next_states = [
            (jug1, b),                              # Fill Jug 1
            (a, jug2),                              # Fill Jug 2
            (0, b),                                 # Empty Jug 1
            (a, 0),                                 # Empty Jug 2
            (max(0, a - (jug2 - b)), min(jug2, a + b)),  # Pour Jug 1 -> Jug 2
            (min(jug1, a + b), max(0, b - (jug1 - a)))   # Pour Jug 2 -> Jug 1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    print("No solution found.")

# Main Program
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

water_jug(jug1, jug2, target)
