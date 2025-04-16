def solution_bfs(graph):
    n = len(graph)
    colored_list = [-1]*n ## to store the color for each vertex. we have only two colors [0 and 1]
    queue = []

    for i in range(n): ## as the graph may not be connected, we need to traverse through all the vertex
        if colored_list[i] == -1: ## if we have not assigned a color[i.e, we have not visited the vertex]
            colored_list[i] = 0 ## initially, assign the color 0 to vertex
            queue.append(i) ## add the vertex for bfs traversal

            while queue: 
                node = queue.pop(0)
                
                for neighbor in graph[node]: ## check each adjacent vertex
                    if colored_list[neighbor] == -1: ## if the vertex is not colored[not visited]
                        colored_list[neighbor] = 1 - colored_list[node] ## assign the color different from the current vertex.
                        queue.append(neighbor) 
                    elif colored_list[neighbor] == colored_list[node]: ## if the adjacent vertex have same color,
                        return False ## this is not a bipartite graph. Hence, return False.
    
    return True ## if we are able to colour all the vertex using only two colors with no adjacent vertex having same color, return true.




graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]

print(solution_bfs(graph))