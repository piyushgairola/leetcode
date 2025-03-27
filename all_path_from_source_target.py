def allPathsSourceTarget(graph):
    stack = []
    visited = []
    n = len(graph) - 1
    result = []

    root = 0

    stack.append(root)
    visited.append(root)
    while stack:
        v = stack.pop(0)
        stack.extend(graph[v])
        if n in graph[v]:
            visited.append(n)
            result.append(visited)
            visited = visited[:-1]
        else:
            visited.append(v)

    return result


if __name__ == '__main__':
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    print(allPathsSourceTarget(graph))