class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root):
        return self.sum_left_leaves(root, is_left=False, sum=0)

    def sum_left_leaves(self, node, is_left, sum):
        if node:
            if is_left and node.left is None and node.right is None:
                sum += node.val

            if node.left:
                sum = self.sum_left_leaves(node.left, True, sum)

            if node.right:
                sum = self.sum_left_leaves(node.right, False, sum)

        return sum


if __name__ == '__main__':
    root = TreeNode(val=1)
    node1 = TreeNode(val=2)
    node2 = TreeNode(val=3)
    root.left = node1
    root.right = node2
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    root.right.left = node3
    root.right.right = node4

    sol_obj = Solution()
    print(sol_obj.sumOfLeftLeaves(root))
