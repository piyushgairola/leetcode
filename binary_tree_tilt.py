class Solution:
    def findTilt(self,root):
        def dfs(node):
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.tilt_sum += abs(l-r)

            return node.val+l+r
        
        self.tilt_sum = 0
        dfs(root)
        return self.tilt_sum


