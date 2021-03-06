def dfsAL(graph, start_node):
    stack = []
    visited = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(list(map(lambda x: x[0], graph[node])))

    return visited

def dfsAM(graph, start_node):
    stack = []
    visited = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for idx, weight in enumerate(graph[node]):
                if weight != 0:
                    stack.append(idx)

    return visited