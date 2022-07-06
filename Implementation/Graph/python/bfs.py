from collections import deque

def bfsAL(graph, start_node):
    queue = deque()
    visited = []
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(list(map(lambda x: x[0], graph[node])))

    return visited

def bfsAM(graph, start_node):
    queue = deque()
    visited = []
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for idx, weight in enumerate(graph[node]):
                if weight != 0:
                    queue.append(idx)

    return visited