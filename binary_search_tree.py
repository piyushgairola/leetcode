class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.node_map = dict()

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            self.node_map[val] = self.root
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left_child is None:
                        curr.left_child = Node(val)
                        self.node_map[val] = curr.left_child
                        curr.left_child.parent = curr
                        return curr.left_child
                    else:
                        curr = curr.left_child

                else:
                    if curr.right_child is None:
                        curr.right_child = Node(val)
                        self.node_map[val] = curr.right_child
                        curr.right_child.parent = curr
                        return curr.right_child
                    else:
                        curr = curr.right_child
