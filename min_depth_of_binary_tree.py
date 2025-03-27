def solution(root):
    if root is None:
        return 0
    
    left_depth = solution(root.left)
    right_depth = solution(root.right)

    if left_depth == 0:
        return right_depth + 1
    
    if right_depth == 0:
        return left_depth+ 1

    return min(left_depth+1, right_depth+1)

