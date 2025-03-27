def solution(node):
    ## to keep track of the visited node
    ## we maintain the dict by making the org_node as key and new_node as values
    ## this helps us to return the new_node for the respective org_node
    visited_dict = {} 

    ## dfs method to clone each node
    def clone(node):
        if node is None:
            return None

        if node in visited_dict:    ## if node is already in visited, we have already created a new_node for it.
            return visited_dict[node]   ## returning the new_node

        new_node = Node(val=node.val)   ## creating a new_node with org_node value
        visited_dict[node] = new_node   ## adding the org_node and new_node to visited_dict

        for neighbor in node.neighbors: ## we need to add all the neighbors of org_node to new_node by cloning them
            new_node.neighbors.append(clone(neighbor))

        return new_node ## return the new_node[root of cloned graph]


    return clone(node)