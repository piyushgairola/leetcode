class Solution:
    val = 0
    def bstToGst(self,root):
        if root:
            self.bstToGst(root.right)
            root.val = self.val = root.val + self.val
            self.bstToGst(root.left)
            return root
