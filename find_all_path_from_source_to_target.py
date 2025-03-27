def allPath(graphs):
    def dfs(curr_node, path_covered):
        if curr_node == n-1:
            return res.append(path_covered)

        else:
            for child in graphs[curr_node]:
                dfs(child, path_covered+[child])

    n = len(graphs)
    res = []
    dfs(0,[0])

    return res


graphs = [[4,3,1],[3,2,4],[3],[4],[]]

print(allPath(graphs))