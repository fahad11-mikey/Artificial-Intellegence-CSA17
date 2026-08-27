from collections import deque

def bfs(graph, start):
    visited = set()          # To track visited nodes
    queue = deque([start])   # FIFO queue for BFS
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)          # Process the node (you can store instead of printing)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
bfs(graph, 'A')
