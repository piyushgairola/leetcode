def leastBricks(wall):
    edge_freq = dict()
    max_freq = 0

    for i in range(len(wall)):
        edge_pos = 0
        for j in range(len(wall[i])-1):
            curr_edge = wall[i][j]
            edge_pos += curr_edge
            edge_freq[edge_pos] = edge_freq.get(edge_pos,0) + 1
            
            max_freq = max(edge_freq[edge_pos], max_freq)


    return len(wall)-max_freq


if __name__ == "__main__":
    wall = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

    print(leastBricks(wall))