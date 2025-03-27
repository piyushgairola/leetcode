class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    l = len(lists)
    res = lists[0]

    for i in range(1,l):
        res = merge2Lists(res,lists[i])

    return res


def merge2Lists(list1,list2):
    # l1 = len(list1)-1
    # l2 = len(list2)-1
    # k = len(list1)+len(list2)-1
    # r = [None]*(k+1)
    head = r = None
    l1 = list1[0]
    l2 = list2[0]

    while(l1.next and l2.next):
        if(l1.val > l2.val):
            if r:
                r.next = l1
            else:
                head = l1
                r = head
            l1 = l1.next
        else:
            if r:
                r.next = l2
            else:
                head = l2
                r = head
            l2 = l2.next
        
        r = r.next
        
        

    while(l1.next):
        r.next = l1
        l1 = l1.next
        r = r.next
    
    while(l2.next):
        r.next = l2
        l2= l2.next
        r = r.next

    return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(5)

    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    node7 = ListNode(2)
    node8 = ListNode(6)
    node7.next = node8

    lists = [[node1,node2,node3],[node4,node5,node6],[node7,node8]]
    print(mergeKLists(lists))

    