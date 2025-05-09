class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self,root):
        def dfs(node,depth):
            if node:
                if depth == len(ans):
                    ans.append(node.val)
                dfs(node.right,depth+1)
                dfs(node.left, depth+1)

        ans = []
        dfs(root,0)
        return ans
