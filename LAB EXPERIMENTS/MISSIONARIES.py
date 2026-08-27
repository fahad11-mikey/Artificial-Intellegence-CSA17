from collections import deque

def is_valid(m, c):
    # Missionaries should not be outnumbered
    return (m == 0 or m >= c) and (3-m == 0 or 3-m >= 3-c)


def missionaries_cannibals():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        m, c, boat = state

        moves = [
            (1,0), (2,0),
            (0,1), (0,2),
            (1,1)
        ]

        for dm, dc in moves:

            if boat == 1:
                new_state = (m-dm, c-dc, 0)
            else:
                new_state = (m+dm, c+dc, 1)

            if (0 <= new_state[0] <= 3 and
                0 <= new_state[1] <= 3 and
                is_valid(new_state[0], new_state[1])):

                queue.append((new_state, path))


solution = missionaries_cannibals()

print("Solution Path:")
for step in solution:
    print(step)
