class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head,n):
    t1 = head
    t2 = head
    while(n>0 and t2.next != None):
        t2 = t2.next
        n-=1

    if n>0:
        return head.next
    
    while(t2.next != None):
        t1 = t1.next
        # if t2.next != None:
        #     t2=t2.next
        # else:
        #     break
        t2 = t2.next
    
    temp = t1.next.next
    t1.next = temp
    
    return head


if __name__ == '__main__':
    head = ListNode(0)
    # node1 = ListNode(1)
    # head.next = node1
    # node2  = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4

    res = removeNthFromEnd(head,1)
    while(res):
        print(res.val)
        res = res.next