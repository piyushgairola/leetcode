class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    l1 = l2 = 0
        
    t1 = headA
    while(t1):
        l1 += 1
        t1 = t1.next
        
    t2 = headB
    while(t2):
        l2 +=1
        t2 = t2.next
        
    if l1<l2:
        d = l2-l1
        t1 = headA
        t2 = headB
        while(d>0):
            t2 = t2.next
            d -=1
    else:
        d = l1-l2
        t1 = headA
        t2 = headB
        while(d>0):
            t1 = t1.next
            d-=1
            
    while(t1 != t2):
        t1 = t1.next
        t2 = t2.next
    
    return t1


if __name__ == "__main__":
    headA = ListNode(0)
    node1 = ListNode(1)
    head.next = node1
    node2  = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4