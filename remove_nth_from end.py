class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n ==1 and not head.next:
            return None

        curr = head
        i = 0
        temp = head

        while curr.next:
            curr = curr.next
            i += 1
            if i > n:
                temp = temp.next

        node = temp.next
        temp.next = node.next

        return head


if __name__ == '__main__':
    head = ListNode(val=1)
    node1 = ListNode(val=2)
    head.next = node1
    # node2 = ListNode(val=3)
    # node1.next = node2
    # node3 = ListNode(4)
    # node2.next = node3
    # node4 = ListNode(5)
    # node3.next = node4

    sol = Solution()
    res = sol.removeNthFromEnd(head, 2)

    temp = res
    while (temp):
        print(temp.val)
        temp = temp.next
