# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root.val == key:
            left_child = root.left
            right_child = root.right
            root = right_child
            while root.left:
                root = root.left

            root.left = left_child

            return root
        if root.left:
            self.deleteNode(root.left, key)
        if root.right:
            self.deleteNode(root.right, key)

        return root


if __name__ == '__main__':
    root = TreeNode(val=5)
    root.left = TreeNode(val = 3)
    root.right = TreeNode(val = 6)
    root.left.left = TreeNode(val = 2)
    root.left.right = TreeNode(val=4)
    root.right.right = TreeNode(val=7)

    sol = Solution()
    res = sol.deleteNode(root,3)
    print(sol.deleteNode(root,3))
