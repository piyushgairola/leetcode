from binary_search_tree import BinarySearchTree


def zig_zag_traversal(root):
    if root is None:
        return None

    result = list()
    q = [root]
    c = 0

    while q:
        c = c+1
        temp = []
        for i in range(len(q)):
            node = q.pop(0)
            temp.append(node.val)
            if node.left_child:
                q.append(node.left_child)
            if node.right_child:
                q.append(node.right_child)

        if c%2==0:
            result.append(temp[::-1])
        else:
            result.append(temp)

    return result


if __name__ == '__main__':
    node_list = list(map(int, input().split()))

    bst = BinarySearchTree()
    for i in node_list:
        bst.insert(i)

    root = bst.root
    result = zig_zag_traversal(root)
    print(result)
