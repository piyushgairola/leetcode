# def solution(root):
#     max_diameter  = 0 

#     def depth(node):
#         if node is None:
#             return 0
        
#         left_depth = depth(node.left)
#         right_depth = depth(node.right_depth)

#         nonlocal max_diameter
#         max_diameter = max(left_depth + right_depth, max_diameter)

#         return max(left_depth, right_depth) + 1

#     depth(root)
#     return max_diameter



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def compute_depths(root, depth=0, depth_map={}):
    if root is None:
        return
    depth_map[root.val] = depth  # Store depth of current node
    compute_depths(root.left, depth + 1, depth_map)  # Recursive call for left child
    compute_depths(root.right, depth + 1, depth_map)  # Recursive call for right child
    return depth_map

# Example Binary Tree
"""
        1
       / \
      2   3
     / \
    4   5
"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Compute depths of each node
depth_map = compute_depths(root)

# Print the depth map
print(depth_map)  
