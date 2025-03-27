def solution(equations, values, queries):

    graph = {}
    answer = []

    def build_graph():
        for idx, (x,y) in enumerate(equations):
            _weighted_node_1 = (y, values[idx])
            _weighted_node_2 = (x, 1/values[idx])

            if y not in graph:
                graph[y] = []
            
            if x not in graph:
                graph[x] = []

            graph[x].append(_weighted_node_1)
            graph[y].append(_weighted_node_2)


    def calculate(start,end, visited, ans):
        if start == end:
            return 
        
        if start in visited:
            return 
        
        visited.add(start)
        
        for node, weight in graph[start]:
            calculate(node, end, visited, ans[0] * weight) 

    build_graph()

    for q1, q2 in queries:
        if q1 not in graph or q2 not in graph:
            answer.append(-1)
        visited = set()
        ans = [1]
        ans = calculate(q1,q2,visited,ans)
        answer.append(ans[0])

    return answer


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]


print(solution(equations, values, queries))