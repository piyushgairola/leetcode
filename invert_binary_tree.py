import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root):
        if root:
            self.invert_tree(root.left)
            self.invert_tree(root.right)

            temp = root.left
            root.left = root.right
            root.right = temp

            return root
        return

    def invertTree(self, root):
        if root == None:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left
        return root

    def preorder(self, root):
        if root:
            print(root.val)
            if root.left:
                self.preorder(root.left)
            if root.right:
                self.preorder(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root_left = TreeNode(2)
    root_right = TreeNode(3)
    root.left = root_left
    root.right = root_right
    root_left.left = TreeNode(4)
    root_left.right = TreeNode(5)

    root_right.left = TreeNode(6)
    obj = Solution()
    t0 = time.time()
    r = obj.invert_tree(root)
    print(time.time() - t0)
    print(r.val)

    t1 = time.time()
    r1 = obj.invertTree(root)
    print(time.time() - t1)
    print(r1.val)

    print(r.left.val) if r.left else print("null")
    print(r.right.val) if r.right else print("null")

    print(r1.left.val) if r1.left else print("null")
    print(r1.right.val) if r1.right else print("null")
