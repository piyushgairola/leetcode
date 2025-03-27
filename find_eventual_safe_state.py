def solution(graph):
    n = len(graph)
    safe_nodes = []
    out_degree = [0 for i in range(n)]

    for i in range(n):
        out_degree[i] += len(graph[i])

    terminal_nodes = [ i for i in range(n) if out_degree[i] == 0]

    for idx, arr in enumerate(graphs):
        if len(arr) > len(terminal_nodes):
            continue
        
        if len(arr) == len(terminal_nodes) and arr == terminal_nodes:
            safe_nodes.append(idx)

        if len(arr) < len(terminal_nodes):
            safe_nodes.append(idx)


    return safe_nodes+terminal_nodes

graphs = [[1,2],[2,3],[5],[0],[5],[],[]]

print(solution(graphs))
