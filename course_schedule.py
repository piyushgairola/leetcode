def solution(numCourses, prerequisites):
    '''
    # this is not optimal representation, 
    # we are using more memory than required as set has higher memory usage than set
    # set would be a better choice for faster lookup which is not required in this case
    # hence, we can use a list of lists to represent the adjacency list

    pre_adj_list = { i:set() for i in range(numCourses)} 
    '''

    pre_adj_list = [[] for i in range(numCourses)]

    visited = [0 for i in range(numCourses)]

    for c1, pre in prerequisites:
        pre_adj_list[pre].append(c1)

    def has_cycle(edge):
        if visited[edge] == -1: # -1 indicates that the node is being visited, hence cycle
            return True

        if visited[edge] == 1: # 1 indicates that the node has been visited and no cycle
            return False

        visited[edge] = -1 # mark the node as being visited

        for i in pre_adj_list[edge]:
            if has_cycle(i):
                return True

        visited[edge] = 1
        return False


    for i in range(numCourses):
        if has_cycle(i):
            return False


    return True


prerequisites = [[1,0],[0,2],[2,1]]
numCourses = 3

print(solution(numCourses, prerequisites))