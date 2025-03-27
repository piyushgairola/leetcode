def solution(graph):
    all_path = []

    def dfs(node, curr_path):
        if node == len(graph) - 1:
            curr_path.append(node)
            all_path.append(curr_path)
        else:
            ## section 1
            ## 
            # curr_path.append(node) 
            # for i in graph[node]:
            #     dfs(i, curr_path)

            ## section 2
            for i in graph[node]:
                dfs(i, curr_path+[node])

    dfs(0, [])
    return all_path

    


graph = [[1,2],[3],[3],[]]

print(solution(graph))
    
