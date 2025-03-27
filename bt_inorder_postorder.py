"""

Solution not correct.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        inorder_idx_map = {}
        n = len(inorder)
        for i, elem in enumerate(inorder):
            inorder_idx_map[elem] = i
        post_idx = n - 1
        return self.buildTreeUtil(postorder, 0, n - 1, post_idx, inorder_idx_map)

    def buildTreeUtil(self, postorder, start, end, post_idx, inorder_idx_map):
        if start > end:
            return None

        node_val = postorder[post_idx]
        post_idx -= 1
        node = TreeNode(val=node_val)

        if start == end:
            return node

        idx = inorder_idx_map[node.val]
        node.right = self.buildTreeUtil(postorder, idx + 1, end, post_idx, inorder_idx_map)
        node.left = self.buildTreeUtil(postorder, start, idx - 1, post_idx, inorder_idx_map)


        return node


def preorder(root):
    if root:
        print(root.val)
    preorder(root.left)
    preorder(root.right)


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]

    sol = Solution()
    root = sol.buildTree(inorder, postorder)

