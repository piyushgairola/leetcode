"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, node):
        if node.next is None:
            node = None
        node.val = node.next.val
        node.next = node.next.next

    def deleteNode(self, node):
        next_node = node.next
        if next_node:
            node.val = next_node.val
            node.next = next_node.next
        else:
            raise Exception("Can't delete the tail node")