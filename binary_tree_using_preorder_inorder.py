class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildtree(preorder,inorder):
    def helper(start,end):
        if start>end:
            return None
        node_val = next(preorder)
        node = TreeNode(node_val)
        idx = inorder_dict[node_val]
        node.left = helper(start,idx-1)
        node.right = helper(idx+1, end)
        return node
    
    preorder = iter(preorder)
    inorder_dict = {}
    n = len(inorder)
    for i,val in enumerate(inorder):
        inorder_dict[val] = i

    root = helper(0,n-1)
    return root

def printTree(root):
    que = []
    que.append(root)

    while(que):
        node = que.pop(0)
        if node:
            print(node.val)
            que.append(node.left)
            que.append(node.right)
        # else:
        #     print("null")
        



preorder = [1,2,4,5,8,9,3,6,7,10,11]
inorder = [4,2,8,5,9,1,6,3,10,7,11]
root = buildtree(preorder, inorder)

printTree(root)







    
