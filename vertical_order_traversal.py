# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root):
        result = self.printLevelOrder(root, result={}, x=0)
        sol = []
        for i in sorted(result.keys()):
            sol.append(result[i])
        return sol

    def height(self,node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            # Use the larger one
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def printGivenLevel(self,root, level,result,x):
        if root is None:
            return
        if level == 1:
            val = root.val
            if x in result.keys():
                result[x].append(val)
            else:
                result[x] = [val]

        elif level > 1:
            self.printGivenLevel(root.left, level - 1,result,x-1)
            self.printGivenLevel(root.right, level - 1,result,x+1)


    def printLevelOrder(self,root,result,x):
        h = self.height(root)
        for i in range(1, h + 1):
            self.printGivenLevel(root, i,result,x)

        return result




if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(5)
    root.left.left.left.right = TreeNode(7)
    root.left.left.right.left = TreeNode(6)
    root.left.left.left.right.left = TreeNode(10)
    root.left.left.left.right.right = TreeNode(8)
    root.left.left.right.left.left = TreeNode(11)
    root.left.left.right.left.right = TreeNode(9)

    sol= Solution().verticalTraversal(root)
    print(sol)