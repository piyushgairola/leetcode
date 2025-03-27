class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minCameraCover(root):
    camera = 0
    covered = {None}

    def dfs(root, parent):
        if root:
            dfs(root.left, root)
            dfs(root.right, root)

            if parent is None and root not in covered or root.left not in covered or root.right not in covered:
                nonlocal camera
                camera += 1
                covered.update({root, parent, root.left, root.right})

    dfs(root,None)
    return camera


if __name__ == '__main__':
    node1 = TreeNode(val=1)
    node2 = TreeNode(val=2)
    node3 = TreeNode(val=3)
    node4 = TreeNode(val=4)
    node5 = TreeNode(val=5)
    node6 = TreeNode(val=6)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node4.left = node6


    print(minCameraCover(node1))